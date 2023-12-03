
def count_batteries_by_health(present_capacities):
  counts= {  
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }  '''name the dict for convinience'''
  rated_cap=120 '''assume'''

  for present_cap in present_capacities:
    soh=round((present_cap/rated_cap)*100) '''given formula'''
    if soh>80.00:
      counts["healthy"]+=1
    elif soh<=80.00 and soh>=62.00:
      counts["exchange"]+=1
    else:
      counts["failed"]+=1
  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
#making all efficient
  present_capacities = [120,120,120,120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 4)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")
#giving empty list
  present_capacities = []
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")

#giving float values
  present_capacities = [113.5, 116.67, 80.7, 95.8, 92.90, 70.8]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
if __name__ == '__main__':
  test_bucketing_by_health()
