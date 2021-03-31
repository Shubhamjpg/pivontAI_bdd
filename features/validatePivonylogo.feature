Feature: pivony Logo

  Scenario: Logo presence on pivony home Page
    Given launch chrome browser
    When open pivony homepage
    Then verify that the logo present on page
    And close browser
