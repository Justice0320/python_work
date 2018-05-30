guest_list = ["frank zappa", "misha zainib", "kurt cobain"]

message = "This is an invitatioin to " + guest_list[0].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[1].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[2].title() + " inviting you for drinks"
print(message)

print("\nI'm afraid " + guest_list[2].title() + " is unable to attend")

del guest_list[2]
guest_list.append("chris turnbull")

print("\n")
print(guest_list)
print("\n")


message = "This is an invitatioin to " + guest_list[0].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[1].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[2].title() + " inviting you for drinks"
print(message)

print("\nWe have been offred a larger table for drinks\nguest_list.py")

guest_list.insert(0, "jimi hendrix")
guest_list.insert(2, "andy murray")
guest_list.append("yoshitaka amano")

message = "This is an invitatioin to " + guest_list[0].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[1].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[2].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[3].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[4].title() + " inviting you for drinks"
print(message)

message = "This is an invitatioin to " + guest_list[5].title() + " inviting you for drinks"
print(message)

print(guest_list)