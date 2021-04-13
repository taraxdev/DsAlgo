class solutions:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
