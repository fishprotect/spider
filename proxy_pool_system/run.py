import manage

def main():
    try:
        s = manage.Manage()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
