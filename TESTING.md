# Testing

Return back to [README.md](README.md) file.

# Table of Contents

- [Code validation](#code-validation)
- [Tested browsers](#tested-browsers)
- [Lighthouse audit](#lighthouse-audit)
- [Manual testing](#manual-testing)
- [User story testing](#user-story-testing)
- [Fixed bugs](#fixed-bugs)

## Code validation

### HTML Validation

All pages have been validated using the W3C Markup Validation Service and contain no errors or warnings that affect site functionality.

### Home page

![Home page screenshot](documentation/validation/html/html-validation-base-home.png)

### About page

![About page screenshot](documentation/validation/html/html-validation-about.png)

### Menu page

![Menu page screenshot](documentation/validation/html/html-validation-menu.png)

### Contact page

![Contact page screenshot](documentation/validation/html/html-validation-contact.png)

### Contact success page

![Contact success page screenshot](documentation/validation/html/html-validation-contact-success.png)

### Login page

![Login page screenshot](documentation/validation/html/html-validation-login.png)

### Logout page

![Logout page screenshot](documentation/validation/html/html-validation-logout.png)

### Sign up page

![Sign up page screenshot](documentation/validation/html/html-validation-signup.png)

### New booking page

![New booking page screenshot](documentation/validation/html/html-validation-bookings-new.png)

### Booking success page

![Booking success page screenshot](documentation/validation/html/html-validation-bookings-success.png)

### My bookings page

![My bookings list page screenshot](documentation/validation/html/html-validation-bookings.png)

### Edit bookings page

![Edit bookings list page screenshot](documentation/validation/html/html-validation-bookings-edit.png)

### 404 page

![404 page screenshot](documentation/validation/html/html-validation-404.png)

### 500 page

![500 page screenshot](documentation/validation/html/html-validation-500.png)

### CSS Validation

I validated all of my CSS files using the recommended W3C Jigsaw CSS Validator, and they passed without any errors.

![CSS validation screenshot](documentation/validation/css/css-validation.png)

### Python Validation

I used the recommended PEP8 CI Python Linter to ensure that all my Python files adhere to proper coding style standards.

## Validation for 'thecove' files

| File name   | Screenshot                                                                      | Notes                                             |
| ----------- | ------------------------------------------------------------------------------- | ------------------------------------------------- |
| asgi.py     | ![asgi.py screenshot](documentation\validation\python\thecove-asgi.png)         | Pass                                              |
| settings.py | ![settings.py screenshot](documentation\validation\python\thecove-settings.png) | Messsage: AUTH_PASSWORD_VALIDATORS lines too long |
| urls.py     | ![urls.py screenshot](documentation\validation\python\thecove-urls.png)         | Pass                                              |
| wsgi.py     | ![wsgi.py screenshot](documentation\validation\python\thecove-wsgi.png)         | Pass                                              |

---

## Validation for 'bookings' files

| File name | Screenshot                                                                   | Notes |
| --------- | ---------------------------------------------------------------------------- | ----- |
| admin.py  | ![admin.py screenshot](documentation\validation\python\bookings-admin.png)   | Pass  |
| apps.py   | ![apps.py screenshot](documentation\validation\python\bookings-apps.png)     | Pass  |
| forms.py  | ![forms.py screenshot](documentation\validation\python\bookings-forms.png)   | Pass  |
| models.py | ![models.py screenshot](documentation\validation\python\bookings-models.png) | Pass  |
| urls.py   | ![urls.py screenshot](documentation\validation\python\bookings-urls.png)     | Pass  |
| views.py  | ![views.py screenshot](documentation\validation\python\bookings-views.png)   | Pass  |

[Return to Table of Contents](#table-of-contents)

## Tested browsers

I tested my deployed project across multiple browsers to ensure compatibility.

### Chrome

![Chrome screenshot](documentation\browsers\browser-chrome.png)

### Firefox

![Firefox screenshot](documentation\browsers\browser-firefox.png)

### Edge

![Edge screenshot](documentation\browsers\browser-edge.png)

[Return to Table of Contents](#table-of-contents)

## Device responsiveness

I tested my deployed project on various devices to verify its responsiveness.

### Mobile - Used Chrome DevTools

![Mobile screenshot](documentation\responsiveness\mobile.png)

### Tablet - Used Chrome DevTools

![Tablet screenshot](documentation\responsiveness\tablet.png)

[Return to Table of Contents](#table-of-contents)

## Lighthouse audit

I used the Lighthouse Audit tool to evaluate my deployed project and identify any significant issues.

### Home page

![Home page screenshot](documentation\lighthouse\lighthouse-desktop-home.png)

### About page

Scored lower on Best Practices due to using Google Maps to embed.

![About page screenshot](documentation/lighthouse/lighthouse-desktop-about.png)

### Menu page

![Menu page screenshot](documentation/lighthouse/lighthouse-desktop-menu.png)

### Contact page

![Contact page screenshot](documentation/lighthouse/lighthouse-desktop-contact.png)

### Login page

![Login page screenshot](documentation/lighthouse/lighthouse-desktop-login.png)

### Logout page

![Logout page screenshot](documentation/lighthouse/lighthouse-desktop-logout.png)

### Sign up page

![Sign up page screenshot](documentation/lighthouse/lighthouse-desktop-signup.png)

### New booking page

![New booking page screenshot](documentation/lighthouse/lighthouse-desktop-bookings-new.png)

### My bookings page

![My bookings list page screenshot](documentation/lighthouse/lighthouse-desktop-bookings.png)

### 404 page

![404 page screenshot](documentation/lighthouse/lighthouse-404.png)

### 500 page

![500 page screenshot](documentation/lighthouse/lighthouse-500.png)

[Return to Table of Contents](#table-of-contents)

## Manual testing

| Feature/Test                                  | Expected Behaviour                                                   | Result |
| --------------------------------------------- | -------------------------------------------------------------------- | ------ |
| **Logo in Navbar**                            | Clicking logo redirects to the homepage                              | Pass   |
| **Navigation Links** (Home, About, Menu, etc) | Each link takes the user to the correct page                         | Pass   |
| **Navbar on Mobile**                          | Navbar collapses into a hamburger menu with working links            | Pass   |
| **Footer Social Links**                       | Clicking opens the link in a new browser tab                         | Pass   |
| **Login Button**                              | Takes the user to the login page                                     | Pass   |
| **Login Form – empty fields**                 | Prevents submission and shows required field messages                | Pass   |
| **Login – wrong username**                    | Displays error message for invalid user                              | Pass   |
| **Login – wrong password**                    | Displays error message for incorrect password                        | Pass   |
| **Login – correct details**                   | Logs user in and redirects to "My Bookings"                          | Pass   |
| **Navbar after login**                        | Updates to show “My Bookings” and “Sign Out”, removes Login/Register | Pass   |
| **Register link on Login Page**               | Redirects user to the registration page                              | Pass   |
| **Registration – empty fields**               | Submission blocked with form error messages                          | Pass   |
| **Registration – username/email exists**      | Prevents submission and shows appropriate error message              | Pass   |
| **Registration – valid new user**             | Creates new account and redirects with login prompt                  | Pass   |
| **Login link on Login Page**                  | Redirects back to login page                                         | Pass   |
| **Logout button**                             | Logs user out and redirects to homepage                              | Pass   |
| **Logout Confirmation**                       | Modal appears to confirm logout action                               | Pass   |
| **“My Bookings” Link (logged in)**            | Opens user’s bookings page                                           | Pass   |
| **“My Bookings” Link (logged out)**           | Redirects to login page                                              | Pass   |
| **My Bookings – Edit Button**                 | Opens edit form with existing booking info pre-filled                | Pass   |
| **My Bookings – Delete Button**               | Triggers a modal to confirm deletion before proceeding               | Pass   |
| **Booking Form – empty**                      | Submission blocked and shows error messages                          | Pass   |
| **Booking Form – logged out**                 | Redirects to login page                                              | Pass   |
| **Booking Form – valid input**                | Saves booking and redirects to “My Bookings” with confirmation       | Pass   |
| **Edit Booking Form – fields pre-filled**     | Displays current booking info in form fields                         | Pass   |
| **Edit Booking – empty fields**               | Submission blocked with validation messages                          | Pass   |
| **Edit Booking – valid update**               | Saves changes and redirects to “My Bookings” with message            | Pass   |
| **Access Edit Booking (logged out)**          | Redirects to login or shows error                                    | Pass   |
| **Invalid URL entered**                       | Loads custom 404 error page                                          | Pass   |
| **404 Page – Home button**                    | Redirects back to the homepage                                       | Pass   |
| **Server Error Triggered**                    | Loads custom 500 error page                                          | Pass   |
| **500 Page – Home button**                    | Redirects to the homepage                                            | Pass   |

[Return to Table of Contents](#table-of-contents)

## User story testing

| **User Story** | **Screenshot** |
|----------------|----------------|
| As a site user, I want to view the homepage and navigate the site so that I can find important information. | ![Homepage](documentation/features/features-home.png) |
| As a site user, I want to create an account so that I can make and manage bookings. | ![Sign Up Page](documentation/features/features-signup.png) |
| As a logged-in user, I want to log into my account so that I can access my bookings. | ![Login Page](documentation/features/features-login.png) |
| As a logged-in user, I want to make a booking so that I can reserve a table at The Cove. | ![Booking Form](documentation/features/features-bookings-new.png) |
| As a logged-in user, I want to view, edit, or cancel my bookings so that I can manage my plans. | ![My Bookings](documentation/features/features-bookings.png) |
| As a logged-in user, I want to log out securely so that my session ends properly. | ![Logout](documentation/features/features-logout.png) |
| As a Cove administrator, I want to manage all bookings so that customer reservations are organised and conflicts avoided. | ![Admin Dashboard](documentation/features/features-bookings.png) |

[Return to Table of Contents](#table-of-contents)

## Fixed bugs

### Bug 1

Fixed correct parth to bookings url.<br><br>
_Original code_:<br>

```py
path('success/', views.booking_success, name='booking_success'),
path('<int:pk>/', views.booking_detail, name='booking_detail'),
```

_New code_:<br>

```py
path('bookings/success/', views.booking_success, name='booking_success'),
path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),
```

### Bug 2

Correctly save booking instance with logged-in user.<br><br>
_Original code_:<br>

```py
form.save()
```

_New code_:<br>

```py
booking.save()
```

### Bug 3

Restrict booking list to show only user's bookings if not staff.<br><br>
_Original code_:<br>

```py
bookings = Booking.objects.all().order_by('-booking_date', '-booking_time')
```

_New code_:<br>

```py
bookings = Booking.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
```

[Return to Table of Contents](#table-of-contents)
