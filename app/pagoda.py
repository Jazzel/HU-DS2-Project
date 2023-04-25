from datetime import date

# Remove city
people = [
    {'item': 'Ramen', 'expiry': date(2002,11,24), 'city': 'Karachi'},
    {'item': 'ice cream', 'expiry': date(2001,12,18), 'city': 'Lahore'},
    {'item': 'chips', 'expiry': date(2003,1,31), 'city': 'Islamabad'}
]

people2 = [
    {'item': 'biscuits', 'expiry': date(2002,10,1), 'city': 'Karachi'},
    {'item': 'juice', 'expiry': date(2003,7,27), 'city': 'Islamabad'},
    {'item': 'drink', 'expiry': date(2004,7,4), 'city': 'Lahore'}
]

class Pagoda:
    def __init__(self):
        self.towers = []

    def insert(self, x):
        # Check if x is already in the towers
        if any(x['expiry'] == person['expiry'] and x['item'] == person['item'] for tower in self.towers for person in tower):
            return x

        # Append element x to the leftmost empty tower
        i = 0
        while i < len(self.towers) and self.towers[i]:
            i += 1
        if i == len(self.towers):
            self.towers.append([x])
        else:
            self.towers[i].append(x)

        # Merge any two towers of equal size
        for j in range(i - 1, -1, -1):
            if len(self.towers[j]) == len(self.towers[j + 1]):
                self.towers[j] = self.merge(self.towers[j], self.towers[j + 1])
                self.towers[j + 1] = []

        # Propagate the smaller of x and the root of the rightmost nonempty tower
        for j in range(len(self.towers) - 1, -1, -1):
            if self.towers[j] and isinstance(self.towers[j][0], dict) and x['expiry'] < self.towers[j][0]['expiry']:
                x, self.towers[j][0] = self.towers[j][0], x
                if j == 0:
                    break
                if len(self.towers[j - 1]) < len(self.towers[j]):
                    self.towers[j - 1] = self.merge(self.towers[j - 1], self.towers[j])
                    self.towers[j] = []
        return x

    def find_min(self):
        if not self.towers:
            raise ValueError('Pagoda is empty')
        elif not self.towers[0]:
            del self.towers[0]
            return self.find_min()
        else:
            return self.towers[0][0]

        
    def merge(self, a, b):
        result = []
        while a and b:
            if a[0]['expiry'] < b[0]['expiry']:
                result.append(a.pop(0))
            elif a[0]['expiry'] > b[0]['expiry']:
                result.append(b.pop(0))
            else:
                if a[0]['item'] < b[0]['item']:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))
        result.extend(a)
        result.extend(b)
        return result

#The class ends here 

pagoda = Pagoda()
merged = pagoda.insert(people[0])
merged = pagoda.insert(people[1])
merged = pagoda.insert(people[2])
merged = pagoda.insert(people2[0])
merged = pagoda.insert(people2[1])
merged = pagoda.insert(people2[2])
sorted_people = []
while True:
    try:
        min_person = pagoda.find_min()
    except ValueError:
        break
    sorted_people.append(min_person)
    pagoda.towers[0].pop(0)
    if not pagoda.towers[0]:
        del pagoda.towers[0]

print("Sorted people:")
for person in sorted_people:
    print(f"{person['item']} ({person['expiry']}), {person['city']}")

# print(sorted(merged, key=lambda x: (x, x['expiry'])))
