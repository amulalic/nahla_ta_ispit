from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_cart_page import YourCartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_saucedemo(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    your_cart_page = YourCartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    products = ["Sauce Labs Bike Light", "Sauce Labs Fleece Jacket"]

    #1. Otvori web stranicu https://www.saucedemo.com/ u maksimiziranom prozoru
    login_page.go_to()

    #2. Popuni "Username" i "Password" polje korištenjem sljedećih vrijednosti:
    #Korisničko ime: standard_user
    #Šifra: secret_sauce
    #3. Klikni "Login" dugme
    login_page.login("standard_user", "secret_sauce")

    #4. Verifikuj da se nalaziš na "Products" web stranici
    assert products_page.is_at() == True

    #5. Klikni "Add to cart" dugme za dva različita proizvoda (po ličnom izboru)
    products_page.add_product(products[0])
    products_page.add_product(products[1])

    #6. Klikni ikonu košarice u gornjem desnom uglu
    your_cart_page.go_to()

    #7. Verifikuj da se nalaziš na "Your Cart" web stranici
    assert your_cart_page.is_at() == True

    #8. Korištenjem imena prethodno dodanih proizvoda, verifikuj da se isti nalaze u košarici
    assert your_cart_page.is_product_in_cart(products[0]) == True
    assert your_cart_page.is_product_in_cart(products[1]) == True

    #9. Klikni "Checkout" dugme
    your_cart_page.checkout()

    #10. Verifikuj da se nalaziš na "Checkout: Your Information" web stranici
    assert checkout_page.is_at() == True

    #11. Popuni sva polja na "Checkout: Your Information" web stranici
    checkout_page.fill("Standard", "User", "71000")

    #12. Klikni "Continue" dugme
    checkout_page.proceed()

    #13. Verifikuj da se nalaziš na "Checkout: Overview" web stranici
    assert checkout_overview_page.is_at() == True

    #14. Korištenjem imena prethodno dodanih proizvoda, verifikuj da se isti nalaze na "Checkout: Overview" web stranici
    assert checkout_overview_page.is_product_selected(products[0]) == True
    assert checkout_overview_page.is_product_selected(products[1]) == True

    #15. Klikni "Finish" dugme na "Checkout: Overview" web stranici
    checkout_overview_page.finish()

    #16. Verifikuj da se nalaziš na "Checkout: Complete!" web stranici
    assert checkout_complete_page.is_at() == True

    #17. Klikni na ikonu izbornika u gornjem lijevom uglu
    #18. Kada se izbornik učita, klikni "Logout" link u izborniku
    products_page.log_out()
    
    #19. Verifikuj da se nalaziš na "Login" stranici
    assert login_page.is_at() == True
