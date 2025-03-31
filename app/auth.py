"""
Program: Routes
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: User authentication routes for Flask  application


Revisions:

"""


from flask import Blueprint, flash, render_template, redirect, request,  url_for
# from app.forms import LoginForm
from urllib.parse import urlparse, urljoin

auth = Blueprint('auth', __name__)

def is_safe_redirect_url(target):
    # Check if the url is safe for redirects 
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return (
        redirect_url.scheme in ('http', 'https') and
        host_url.netloc == redirect_url.netloc
    )

# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     head_title = 'Login'
#     page_title = 'Portfolio Login'

#     pass
#     return render_template('login.html', 
#                                head_title=head_title,
#                                page_title=page_title,
#                                form=form
#                                )


# @auth.route('/logout/', methods=['GET', 'POST'])
# # @login_required
# def logout():
#     # logout_user()
#     flash('Logged out successfully!', 'success')

#     next_page = request.form.get('next') or request.args.get('next') 
#     if next_page and is_safe_redirect_url(next_page):
#         return redirect(next_page)
#     return redirect(url_for('pages.index'))


# @auth.route('/signup/', methods=['GET', 'POST'])
# def signup():
#     form = SignupForm()
#     head_title = 'Sign Up'
#     page_title = 'Portfolio Sign Up'

#     # Reroute to index if already logged in
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('pages.index'))

#     if form.validate_on_submit():
#         # user = User(username=form.username.data, email=form.email.data)
        
#         # user.set_password(form.password.data)

#         # db.session.add(user)
#         # db.session.commit()

#         # flash(f'{form.username.data} successfully signed up' , 'success')
#         # flash(f'{user.username} successfully signed up', 'success')

#         # Check the 'next' parameter for safe redirection
#         next_page = request.form.get('next') or request.args.get('next') 

#         if next_page and is_safe_redirect_url(next_page):
#             # Redirect safely
#             return redirect(next_page)
        
#         # Fallback to a default page
#         return redirect(url_for('auth.login'))
    
#     return render_template('signup.html', 
#                                head_title=head_title,
#                                page_title=page_title, 
#                                form=form)