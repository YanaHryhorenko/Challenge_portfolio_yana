from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//*[text()='Main_page']"
    players_button_xpath = "//*[text()='Players']"
    select_language_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    add_player_button_xpath = "//*[text()='Add player']"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    players_count_box_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]"
    matches_count_box_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[2]"
    last_created_player_button = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    reports_count_box_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[3]"
    events_count_box_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]"
    last_updated_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_created_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    last_updated_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
    last_updated_report_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"
