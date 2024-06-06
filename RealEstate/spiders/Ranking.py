import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
import time


class RankingSpider(scrapy.Spider):
    name = "Ranking"
    allowed_domains = ["timeshighereducation.com"]
    start_urls = ['https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking?page=3#']

    def __init__(self, *args, **kwargs):
        super(RankingSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
    def parse(self, response):
        self.log("Visited %s" % response.url)

        self.driver.get(response.url)
        time.sleep(5)  # Wait for JavaScript to load the content

        rows = self.driver.find_elements(By.CSS_SELECTOR, 'tr[role="row"]')
        if rows:
            self.logger.info(f"Found {len(rows)}")
        else:
            self.logger.warning("No rows found")

        for row in rows:
            try:
                rank = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
            except Exception as e:
                self.log(f"Error finding rank: {str(e)}")
                rank = ''
            
            try:
                name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) a.ranking-institution-title').text
            except Exception as e:
                self.log(f"Error finding name: {str(e)}")
                name = ''

            try:
                country = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) div.location span a').text
            except Exception as e:
                self.log(f"Error finding country: {str(e)}")
                country = ''

            try:
                number_of_students = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
            except Exception as e:
                self.log(f"Error finding number_of_students: {str(e)}")
                number_of_students = ''

            try:
                student_staff_ratio = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
            except Exception as e:
                self.log(f"Error finding student_staff_ratio: {str(e)}")
                student_staff_ratio = ''

            try:
                intl_students_percentage = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
            except Exception as e:
                self.log(f"Error finding intl_students_percentage: {str(e)}")
                intl_students_percentage = ''

            try:
                female_male_ratio = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
            except Exception as e:
                self.log(f"Error finding female_male_ratio: {str(e)}")
                female_male_ratio = ''

            try:
                isr_percentage = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
            except Exception as e:
                self.log(f"Error finding isr_percentage: {str(e)}")
                isr_percentage = ''

            yield {
                'rank': rank.strip() ,
                'name': name.strip(),
                'country': country.strip() ,
                'number_of_students': number_of_students.strip(),
                'student_per_staff': student_staff_ratio.strip() ,
                'intl_students_percentage': intl_students_percentage.strip(),
                'female_male_ratio': female_male_ratio.strip(),
                'isr_percentage': isr_percentage.strip(),
            }


    