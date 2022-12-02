from faker import Faker
faker=Faker("pl_PL")
for x in range(10):
    print(faker.first_name(),faker.last_name(), faker.email(), faker.phone_number(), faker.city())

print(faker.word())
print(faker.paragraph())