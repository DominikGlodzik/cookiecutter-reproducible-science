import shutil

def main():
    # Remove binder directory if not wanted
    if '{{ cookiecutter.binder_integration }}' == "FALSE":
        shutil.rmtree("binder")

if __name__ == '__main__':
    main()
