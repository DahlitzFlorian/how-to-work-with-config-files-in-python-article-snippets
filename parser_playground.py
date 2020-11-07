from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

print(f"Sections: {config.sections()}")
print(f'Does a section called "admin" exist: {config.has_section("admin")}')
print(f'Does a section called "user" exist: {config.has_section("user")}')

print(f'Options: {config.options("admin")}')
print(f'"admin_page" in "admin" section: {config.has_option("admin", "admin_page")}')

print("admin_page" in config["admin"])
print(config["admin"]["admin_page"])

config.add_section("unknown")
print(f'Sections: {config.sections()}')

config.remove_section("unknown")
print(f'Sections: {config.sections()}')

config.set("admin", "admin_page", "false")
config.remove_option("admin", "moderator_page")
print(f'Options in "admin" section: {config.items("admin")}')

with open("config1.ini", "w") as f:
    config.write(f)
