import os


def get_config():
    args = {
        "SECRET_KEY": str(os.urandom(25)),
        "DB_PATH": "",
        "DEBUG": "0"
    }

    return args


def generate(path, config):
    parsed_args = [f"{key}={config[key]}" for key in config]

    with open(path, "a") as file:
        for line in parsed_args:
            file.write(f"{line}\n")


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    env_path = os.path.join(current_dir, ".env")

    if os.path.exists(env_path):
        print("Removing existing .env file...")

        os.remove(env_path)

    print("Generating .env config file...")

    generate(env_path, get_config())

    print("Generated .env config file...")


if __name__ == '__main__':
    main()
