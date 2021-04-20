friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "Michael"]

friends_lower = set([n.lower() for n in friends])
guests_lower = set([n.lower() for n in guests])


present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)



#============

friends = ["Rolf", "ruth", "charlie", "Jen"]
time_sience_seen = [3,7,15,11]

long_timers = {
  friends[i]: time_sience_seen[i]
  for i in range(len(friends))
  if time_sience_seen[i] > 5
}

print(long_timers)