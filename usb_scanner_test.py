from scanner import barcode_reader
if __name__ == '__main__':
    try:
        while True:
            upcnumber = barcode_reader()
            print(upcnumber)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
    except Exception as err:
        print(err)
