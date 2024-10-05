import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_reviews():
    driver = webdriver.Chrome()  
    driver.get('https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/')

    reviews_data = []

    
    for page_num in range(1, 5):  
        driver.get(f'https://www.amazon.in/Apple-New-iPhone-12-128GB/product-reviews/B08L5TNJHG/?pageNumber={page_num}')
        time.sleep(3)  
        reviews = driver.find_elements(By.CSS_SELECTOR, "div[data-hook='review']")  

        for review in reviews:
            title = review.find_element(By.CSS_SELECTOR, "a[data-hook='review-title'] span:nth-of-type(2)").text
            text = review.find_element(By.CSS_SELECTOR, "span[data-hook='review-body']").text
            rating = review.find_element(By.CSS_SELECTOR, "i[data-hook='review-star-rating'] span").get_attribute('innerHTML').split(' ')[0]
            try:
                format_strip_element = review.find_element(By.CSS_SELECTOR, 'a[data-hook="format-strip"]')
                format_text = format_strip_element.text

                color = "Unknown"
                style_name = "Unknown"
                
                if "Colour:" in format_text and "Size:" in format_text:
                    
                    color = format_text.split("Colour:")[1].split("Size:")[0].strip()
                    
                    style_name = format_text.split("Size:")[1].split("Pattern Name:")[0].strip()
            except Exception as e:
                color = "Not Available"
                style_name = "Not Available"
                print(f"Error extracting color/size: {e}")

            verified = "Yes" if len(review.find_elements(By.CSS_SELECTOR, 'span[data-hook="avp-badge"]')) > 0 else "No"

            reviews_data.append({
                'title': title,
                'text': text,
                'rating': rating,
                'style_name': style_name,
                'color': color,
                'verified_purchase': verified
            })

    driver.quit()


    df = pd.DataFrame(reviews_data)

    df.to_excel('reviews.xlsx', index=False)

    return reviews_data

scrape_reviews()