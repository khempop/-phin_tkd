from django.urls import path

from pages.views import (
authentication_signin_basic,
authentication_signin_cover,
authentication_signup_basic,
authentication_signup_cover,
authentication_pass_reset_basic,
authentication_pass_reset_cover,
authentication_lockscreen_basic,
authentication_lockscreen_cover,
authentication_logout_basic,
authentication_logout_cover,
authentication_success_msg_basic,
authentication_success_msg_cover,
authentication_twostep_basic,
authentication_twostep_cover,
authentication_404_basic,
authentication_404_cover,
authentication_404_alt,
authentication_500,
authentication_pass_change_basic,
authentication_pass_change_cover,
authentication_offline,
pages_starter,
pages_profile,
pages_profile_settings,
pages_team,
pages_timeline,
pages_faqs,
pages_pricing,
pages_gallery,
pages_maintenance,
pages_coming_soon,
pages_sitemap,
pages_search_results,

pages_landing,
pages_nft_landing,
pages_job_landing,
pages_privacy_policy,
pages_term_conditions,

custom_404,
custom_500,

)

app_name = "pages"

urlpatterns = [
    # Authentication
    path("authentication/signin-basic",view =authentication_signin_basic,name="authentication.signin_basic"),
    path("authentication/signin-cover",view =authentication_signin_cover,name="authentication.signin_cover"),
    path("authentication/signup-basic",view =authentication_signup_basic,name="authentication.signup_basic"),
    path("authentication/signup-cover",view =authentication_signup_cover,name="authentication.signup_cover"),
    path("authentication/password-reset-basic",view =authentication_pass_reset_basic,name="authentication.pass_reset_basic"),
    path("authentication/password-reset-cover",view =authentication_pass_reset_cover,name="authentication.pass_reset_cover"),
    path("authentication/lockscreen-basic",view =authentication_lockscreen_basic,name="authentication.lockscreen_basic"),
    path("authentication/lockscreen-cover",view =authentication_lockscreen_cover,name="authentication.lockscreen_cover"),
    path("authentication/logout-basic",view =authentication_logout_basic,name="authentication.logout_basic"),
    path("authentication/logout-cover",view =authentication_logout_cover,name="authentication.logout_cover"),
    path("authentication/success-msg-basic",view =authentication_success_msg_basic,name="authentication.success_msg_basic"),
    path("authentication/success-msg-cover",view =authentication_success_msg_cover,name="authentication.success_msg_cover"),
    path("authentication/two-step-authentication-basic",view =authentication_twostep_basic,name="authentication.twostep_basic"),
    path("authentication/two-step-authentication-cover",view =authentication_twostep_cover,name="authentication.twostep_cover"),
    path("authentication/404-basic",view =authentication_404_basic,name="authentication.404_basic"),
    path("authentication/404-cover",view =authentication_404_cover,name="authentication.404_cover"),
    path("authentication/404-alt",view =authentication_404_alt,name="authentication.404_alt"),
    path("authentication/500",view =authentication_500,name="authentication.500"),
    path("authentication/pass-change-basic",view =authentication_pass_change_basic,name="authentication.pass_change_basic"),
    path("authentication/pass-change-cover",view =authentication_pass_change_cover,name="authentication.pass_change_cover"),
    path("authentication/offline",view =authentication_offline,name="authentication.offline"),
    
    # Pages
    path("pages/starter-page",view =pages_starter,name="pages.starter"),
    path("pages/profile",view =pages_profile,name="pages.profile"),
    path("pages/profile-settings",view =pages_profile_settings,name="pages.profile_settings"),
    path("pages/team",view =pages_team,name="pages.team"),
    path("pages/timeline",view =pages_timeline,name="pages.timeline"),
    path("pages/faqs",view =pages_faqs,name="pages.faqs"),
    path("pages/pricing",view =pages_pricing,name="pages.pricing"),
    path("pages/gallery",view =pages_gallery,name="pages.gallery"),
    path("pages/maintenance",view =pages_maintenance,name="pages.maintenance"),
    path("pages/coming-soon",view =pages_coming_soon,name="pages.coming_soon"),
    path("pages/sitemap",view =pages_sitemap,name="pages.sitemap"),
    path("pages/search-results",view =pages_search_results,name="pages.search_results"),

    path("pages/landing",view = pages_landing, name="pages.landing"),
    path("pages/nft-landing",view=pages_nft_landing,name="pages.nft_landing"), 
    path("pages/job-landing",view=pages_job_landing,name="pages.job_landing"),
    
    path("pages/privacy-policy",view=pages_privacy_policy,name="pages.privacy_policy"),
    path("pages/term-conditions",view=pages_term_conditions,name="pages.term_conditions"), 

    path("pages/privacy-policy",view=pages_privacy_policy,name="pages.privacy_policy"),
    path("pages/term-conditions",view=pages_term_conditions,name="pages.term_conditions"), 

      
] 

