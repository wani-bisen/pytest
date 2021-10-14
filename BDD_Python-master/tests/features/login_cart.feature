Feature: Login And Cart
    As a customer
    I want to be able to login to the website
    so I can check my account
    Add item to cart
    and delete item from cart

    Scenario: Invalid Customer login to the application
    Given I am in the website
    When I press Sign in
    When I pass my e-mail: "test" and my password: "wb"
    Then I can see alert

Scenario: Customer login to the application
    Given I am in the website
    When I press Sign in
    When I pass my e-mail: "testwb@gmail.com" and my password: "waniwani"
    Then I can see my account

    Scenario: Add item to cart
    Given I am in the homepage of website
    When I navigate to any item
    When I press Add to Cart button
    Then I can see product added pop up

Scenario: Delete item from cart
    Given I am in the homepage of website
    When I navigate to cart page
    When I click on delete icon for added item
    Then I can see empty cart message