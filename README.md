E-Commerce Test Automation Project with Selenium & Python

This project demonstrates end-to-end automation testing for the e-commerce website AutomationExercise using Selenium, Python, and Pytest.

▶️ Project Highlights

  •  Automated test scenarios for Signup, Login, Checkout, and other key user flows.
  
  •  Follows Page Object Model (POM) for maintainable and reusable test code.
  
  •  Implements data-driven testing using Faker for random but realistic test data.
  
  •  Clean code structure: separation of test data, page objects, and test scripts.

▶️ Test Coverage
This project covers key user flows of the e-commerce website, including:

➊ Signup & Account Creation

  • Registering a new user with complete personal and address details
  
  • Handling duplicate email validation

➋ Login

  • Logging in with correct and incorrect credentials

  • Validating input formats and required fields

➌ Product Interaction

  • Adding products to cart from the homepage

  • Viewing the cart and verifying product details

➍ Contact Us

  • Submitting the contact form with valid information

➎ Checkout Process

  • Proceeding through the checkout flow with a registered user

  • Verifying address information and confirming the order

▶️ Tools & Tech Stack

Language: Python

  • Test Framework: Pytest

  • Automation Tool: Selenium WebDriver

  • Data Generation: Faker

  • Reporting: (Optional) Allure Report

▶️ Learning & Contribution

This project was built as part of a self-learning journey in automation testing. The test scenarios were originally created manually and then automated with guidance and improvement using AI assistance. 

The goal was to:

  • Practice writing clean and maintainable automation code

  • Understand testing concepts like element locating, flow control, and validations

  • Build confidence in using Selenium and Pytest for real-world testing

▶️ How to Run the Tests
```bash
1. Clone the repository:
   git clone https://github.com/bewishguy/E-Commerce-Test-Automation-with-Selenium.git
   cd E-Commerce-Test-Automation-with-Selenium
   
3. Navigate into the project:
  cd E-Commerce-Test-Automation-with-Selenium

4. Install dependencies:
  pip install -r requirements.txt

5. Run tests:
  pytest tests/

📄 License
This project is for educational purposes and is open to further improvement and collaboration.
