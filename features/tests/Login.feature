# Created by Alex Kardash at 10/26/19
Feature: Login
  Check user can login with valid username and password

  Background:
    Given I open home page

  Scenario: Valid login
    Given I open url: "/w/index.php?title=Special:UserLogin"
    When I log in

  Scenario Outline: Invalid login
    Given I open url: "/w/index.php?title=Special:UserLogin"
    When I type "<username>" in username field
    When I type "<password>" in password field
    When I click button with text "Log in"
    Then I see element with text "<text>"

    Examples:
      | username     | password     | text                                                 |
      | qwerqwer     | qwerqwer     | Your password must be different from your username.  |
      | 1234qwerqwer | 1234qwerqwer | Incorrect username or password entered.              |
      | !@#$qwerqwer | !@#$qwerqwer | The supplied credentials could not be authenticated. |

  Scenario: Invalid login - data table
    Then I see validation message for
      | username     | password     | text                                                 |
      | qwerqwer     | qwerqwer     | Your password must be different from your username.  |
      | 1234qwerqwer | 1234qwerqwer | Incorrect username or password entered.              |
      | !@#$qwerqwer | !@#$qwerqwer | The supplied credentials could not be authenticated. |
