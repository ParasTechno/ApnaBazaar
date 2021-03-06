from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('product/<int:id>/',views.product),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path("profile/",views.profile),
    path("sellerProfile/",views.sellerProfile),
    path("updateProfile/",views.updateprofile),
    path("addProduct/",views.addProduct),
    path("deleteProduct/<int:num>/",views.deleteProduct),
    path('editProduct/<int:num>/',views.editProduct),
    path('buyerProfile/',views.buyerProfile),
    path("wishlist/<int:num>/",views.wishlistPage),
    path("deleteWishlist/<int:num>/",views.deleteWishlist),
    path("cart/",views.cartPage),
    path("deleteCart/<int:id>/",views.deleteCart),
    path('checkout/',views.checkout),
    path('confirm/',views.confirmationPage),
    path('paymentSuccess/',views.paymentSuccess),
    path('subscribe/',views.subscribePage),
    path('contact/',views.contactUS),
    path('about/',views.about),
    path('forgetPassword/',views.forgetPassword),
    path('confirmOTP/<str:username>/',views.confirmOTP),
    path('enterPassword/<str:username>/',views.enterPassword),
    path('deleteCheckout/<int:num>/',views.checkoutDelete),
    path('paynow/<int:num>/',views.paynow),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
