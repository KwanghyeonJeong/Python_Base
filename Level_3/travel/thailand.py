class ThailandPackage:
    def detail(self):
        print("[Thailand Package 3 nights and 5 days] Travel to Bangkok, Pattaya (Night Market Tour) $ 500")

# This may indicate where the module is used.
if __name__ == "__main__":
    print("Thailand module use direct")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand module call")

