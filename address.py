#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 6 2022
# This program asks the user for an address
# which then prints out a mailing address.


# This function is used to format the function
def format_address(
    name, question, street_num, street_name, city, province, postal_code, apt_num=None
):
    # Formats the strings and put them as uppercase
    can_post_address = (
        name.upper()
        + "\n"
        + street_num
        + " "
        + street_name.upper()
        + "\n"
        + city.upper()
        + " "
        + province.upper()
        + " "
        + postal_code.upper()
    )

    # Add the apartment number if the user lives in one
    if question == "y":
        can_post_address = (
            name.upper()
            + "\n"
            + apt_num
            + "-"
            + street_num
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )
    # It then returns the address back to the main function
    return can_post_address


# This main function gets the user's address
def main():
    # This sets default value
    apt_num_user = None

    # Get the info from the user
    user_name = input("Enter your full name: ")
    user_apt = input("Do you live in an apartment? (y/n): ")

    # This checks if the user lives in an apartment
    if user_apt == "y":
        apt_num_user = input("Enter your apartment number: ")

    # Gets the rest of the user's address
    street_num_user = input("Enter your street number: ")
    street_name_user = input("Enter your street name and type (Main St.): ")
    user_city = input("Enter your city: ")
    province_user = input("Enter your province (as the first two letters): ")
    postal_user = input("Enter your postal code: ")

    # This assigns a variable to the formatted address
    if apt_num_user is not None:
        user_address = format_address(
            user_name,
            user_apt,
            street_num_user,
            street_name_user,
            user_city,
            province_user,
            postal_user,
            apt_num_user,
        )
    else:
        user_address = format_address(
            user_name,
            user_apt,
            street_num_user,
            street_name_user,
            user_city,
            province_user,
            postal_user,
        )
    # This displays the user's formatted address
    print("")
    print("Your mailing address is:\n")
    print(user_address)


if __name__ == "__main__":
    main()
