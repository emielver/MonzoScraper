class Author:

    def __init__(self, name, position):
        self.name = name
        self.positions = [position]
        self.gender = ''
        self.blogs = []


    def add_blog(self, blog):
        self.blogs.append(blog)

    def add_position(self, position):
        self.positions.append(position)

    def set_gender(self, gender):
        self.gender = gender

    def get_name(self):
        return self.name

    def get_cmp_name(self):
        return "".join(self.name.lower().split())

    def get_position(self):
        return self.position[0]

    def get_cmp_position(self):
        return "".join(self.positions[0].lower().split())

    def get_all_positions(self):
        return self.positions

    def get_blogs(self):
        return self.blogs

    def get_number_blogs(self):
        return len(self.blogs)

    def get_gender(self):
        return self.gender

    def cmp_strings(self, str1, str2):
        return "".join(str1.lower()) == "".join(str2.lower())

    def has_name(self, potential):
        return self.cmp_strings(self.name, potential)

    def has_position(self, potential):
        for position in self.positions:
            if self.cmp_strings(position, potential):
                return True
        return False
