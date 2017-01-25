import journal_2


def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------------------------')
    print('              Journal App')
    print('---------------------------------------')


def run_event_loop():
    print('What would you like to do with your journal')
    print()
    cmd = 'Empty'
    journal_name = 'Default'
    journal_data = journal_2.load(journal_name)

    while cmd != 'x' and cmd:

        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("I'm sorry I do not understand your entry of {}.".format(cmd))

    print()
    print("You're finished.")
    journal_2.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal_2.add_entry(text, data)


if __name__ == '__main__':
    main()
