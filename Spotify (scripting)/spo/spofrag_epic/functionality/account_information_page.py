from spo.spofrag_epic.model.user_information_model import (
    UserInformationModel as user_model,
)

from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler
from spo.spofrag_epic.page_object.account_information_pom import (
    AccountInformationPOM as account_pom,
)
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


class AccountInformationPage(account_pom):
    driver_factory = None

    def __init__(self, driver_factory):
        super().__init__(driver_factory)
        self.driver_factory = driver_factory

    def verify_account_page_presented(self, __user_model: user_model) -> bool:
        __is_check: bool = False

        waiter.wait_for_page_fully_loaded(AccountInformationPage.driver_factory)

        waiter.wait_element_until_visible(self.driver_factory,
                                          (locator_type.get_xpath_type(), "//tr[2]//td[2]"),
                                          time_out=const.TIME_OUT_15S,
                                          is_long_wait=True)

        act_usr_email_or_username: str = ui_handler.get_text_from_element(self,
                                                                          exp_element=account_pom.get_lbl_email_or_username(
                                                                              self))
        act_dob: str = ui_handler.get_text_from_element(self, account_pom.get_lbl_dob(self))
        act_nation: str = ui_handler.get_text_from_element(self, account_pom.get_lbl_nation(self))

        # verifying whether User successfully logged in or not
        if (asserter.verify_string_is_equal(__user_model.get_user_email_or_username(), act_usr_email_or_username)
                and asserter.verify_datetime(__user_model.get_user_dob(), act_dob)
                and asserter.verify_string_is_equal(__user_model.get_user_nation(), act_nation)):

            return not __is_check
        else:

            return __is_check

    def click_on_spotify_logo(self):

        waiter.wait_element_until_visible(self.driver_factory,
                                          (locator_type.get_xpath_type(),
                                           "//a[contains(@data-tracking, 'spotify-logo')]"),
                                          time_out=const.TIME_OUT_15S,
                                          is_long_wait=True)

        ui_handler.click_on_element(self, account_pom.get_btn_spotify_logo(self))
