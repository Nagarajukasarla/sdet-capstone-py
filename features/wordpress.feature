Feature: WordPress Website Testing

Scenario: Verify title of WordPress page
    Given Launch the WordPress website
    Then Verify the page title

Scenario: Navigate to Themes
    Given Launch the WordPress website
    When Mouse hover on Extend
    And Click on Themes
    Then Verify themes page is displayed

Scenario: Search for a theme
    Given Launch the WordPress website
    When Mouse hover on Extend
    And Click on Themes
    And Search for theme "astra"
    Then Verify themes are displayed