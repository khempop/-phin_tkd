from django.urls import path
from subscribers.views import(
    subscribers_purchase_view,
    subscribers_checkout_view,
    subscribers_status_view,
    subscribers_success_view,
    subscribers_cancel_view
)
app_name = "subscribers"

urlpatterns = [
    #subscription
    path("subscriber/purchase", view=subscribers_purchase_view, name="subscribers.purchase"),
    path("subscriber/checkout", view=subscribers_checkout_view, name="subscribers.checkout"),
    path("subscriber/status", view=subscribers_status_view, name="subscribers.status"),
    path("subscriber/success/<str:session_id>", view=subscribers_success_view, name="subscribers.success"),
    path("subscriber/cancel", view=subscribers_cancel_view, name="subscribers.cancel"),

]
