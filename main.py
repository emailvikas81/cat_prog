import json
import urllib.request


class CatFinder():
    def find_cats(self, json_url):
        """ Function to consume the json and output a list of all the cats in alphabetical order
            under a heading of the gender of their owner.
            :param json_url: JSON web-service URL
            :return flist, mlist: lists containing cat names for female & male owners respectively
        """
        flist = []
        mlist = []

        try:
            with urllib.request.urlopen(json_url) as url:  # Supports Python3 only
                json_data = json.loads(url.read().decode())

            for person in json_data:
                if person.get('pets') is not None:
                    for pet in person.get('pets'):
                        if pet['type'] == 'Cat':
                            if person.get('gender') == 'Female':
                                flist.append(pet.get('name'))
                            else:
                                mlist.append(pet.get('name'))

            return flist, mlist
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    json_url = "http://agl-developer-test.azurewebsites.net/people.json"
    app = CatFinder()
    flist, mlist = app.find_cats(json_url)

    print("Female \n %s" % sorted(flist))
    print("Male \n %s" % sorted(mlist))
