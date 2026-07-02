from client import OrderHistoryClient
def main():
    c = OrderHistoryClient()
    print(c.lookup_history("customer@test.com"))
if __name__ == '__main__':
    main()
