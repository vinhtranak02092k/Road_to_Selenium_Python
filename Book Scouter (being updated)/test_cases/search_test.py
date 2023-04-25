import pytest

from common.common_operation_helpers import CommonOperatorHelper as common_ope
from common.constants import Constants as const
from page_objects.onboard_experience.home_page import HomePage as home_page
from page_objects.onboard_experience.profile_page import ProfilePage as profile_page
from page_objects.onboard_experience.sign_up_page import SignUpPage as sign_up
from utilities.read_properties import ReadGlobalVariables as read_global_vars
from common.common_waitings import CommonWaitings as waiter

# must have to retrieve the setup method from fixture
from test_cases.abstract_test import setup


@pytest.mark.usefixtures("setup")
class Test_Search:
    __base_url: str = read_global_vars.get_application_url()
    __passed_stt: str = const.TC_PASSED_STATUS
    __failed_stt: str = const.TC_FAILED_STATUS
    __function_test: str = const.TC_SEARCH_FUNCTION

    def test_search_001(self, setup):
        __tc_id: str = "001"
        __search_key: str = "a"

        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.execute_search(self, __search_key)
        waiter.sleep(self, 3)
