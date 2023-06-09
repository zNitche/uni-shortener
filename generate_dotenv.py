import os
import secrets


def get_main_config():
    args = {
        "SECRET_KEY": secrets.token_hex(32),
        "DB_PATH": "",
        "LOGS_PATH": "",
        "DEBUG": "0",
        "ALLOWED_HOSTS": "",
    }

    return args


def get_redis_config():
    args = {
        "REDIS_PASSWORD": secrets.token_hex(32),
    }

    return args


def generate(path, config):
    parsed_args = [f"{key}={config[key]}" for key in config]

    with open(path, "a") as file:
        for line in parsed_args:
            file.write(f"{line}\n")


def generate_main_env(env_path):
    if os.path.exists(env_path):
        print("Removing existing .env file...")

        os.remove(env_path)

    print("Generating .env config file...")

    generate(env_path, get_main_config())

    print("Generated .env config file...")


def generate_redis_env(env_path):
    if os.path.exists(env_path):
        print("Removing existing redis .env file...")

        os.remove(env_path)

    print("Generating redis .env config file...")

    generate(env_path, get_redis_config())

    print("Generated redis .env config file...")


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    main_env_path = os.path.join(current_dir, ".env")
    generate_main_env(main_env_path)

    redis_env_path = os.path.join(current_dir, "redis.env")
    generate_redis_env(redis_env_path)


if __name__ == '__main__':
    main()
