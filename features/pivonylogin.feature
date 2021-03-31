Feature: pivony Login

  Scenario: Login to pivony with valid parameters
    Given I launch chrome browser
    When I open pivony homepage
    And Enter username "nipadoh547@asfalio.com" and password "Shubham@10"
    And Click on login button
    Then user must successfully login to the Dashborad page

