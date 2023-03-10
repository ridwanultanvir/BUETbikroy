from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('user_products/', views.user_products, name = 'user_products'),
    path('divs/', views.divs, name = 'divs'),
    path('product/<int:product_id>', views.product_desc, name = 'product_desc'),
    path('contacts_list/<int:product_id>', views.contacts_list, name = 'contacts_list'),
    path('categories/', views.categories, name = 'categories'),
    path('categories/<int:cat_id>', views.spec_cat, name = 'spec_cat'),
    path('categories/<int:cat_id>/<int:subcat_id>', views.subcat, name = 'subcat'),
    path('divs/<int:div_id>', views.spec_div, name = 'spec_div'),
    path('ad_product/', views.ad_product, name = 'ad_product'),
    path('ad/', views.ad, name = 'ad'),
    path('success/', views.success, name = 'success'),
    path('signup/', views.signup, name = 'signup'),
    path('new_user/', views.new_user, name = 'new_user'),
    path('delete_product/<int:product_id>', views.delete_product, name = 'delete_product'),
    path('edit_product/<int:product_id>', views.edit_product, name = 'edit_product'),
    path('edit_product_action/<int:product_id>', views.edit_product_action, name = 'edit_product_action'),
    path('profile/', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('edit_profile_action/', views.edit_profile_action, name = 'edit_profile_action'),
    path('check_delete/', views.check_delete, name = 'check_delete'),
    path('success_delete/', views.success_delete, name = 'success_delete'),
    path('login/', views.user_login, name = 'login'),
    path('chat/<int:product_id>', views.chat, name = 'chat'),
    path('chat_with_contact/<int:product_id>/<int:contact_id>', views.chat_with_contact, name = 'chat_with_contact'),
    path('ad_chat/<int:product_id>', views.ad_chat, name = 'ad_chat'),
    path('contact_chat_action/<int:product_id>/<int:contact_id>', views.contact_chat_action, name = 'contact_chat_action'),
    path('logout/', views.user_logout, name = 'logout'),
    path('areas/<int:area_id>', views.spec_area, name = 'spec_area'),
    path('register_company/', views.register_company, name = 'register_company'),
    path('add_company/', views.add_company, name = 'add_company'),
    path('offered_jobs/<int:comp_id>', views.offered_jobs, name = 'offered_jobs'),
    path('job_desc/<int:job_id>', views.job_desc, name = 'job_desc'),
    path('job_list/<int:type_id>', views.job_list, name = 'job_list'),
    path('user_jobs/', views.user_jobs, name = 'user_jobs'),
    path('apply_job/<int:job_id>', views.apply_job, name = 'apply_job'),
    path('applicants_list/<int:job_id>', views.applicants_list, name = 'applicants_list'),
    path('add_job/<int:comp_id>', views.add_job, name = 'add_job'),
    path('job_types/', views.job_types, name = 'job_types'),
    path('applicant_info/<int:applicant_id>', views.applicant_info, name = 'applicant_info'),
]
