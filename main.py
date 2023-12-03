
def count_batteries_by_health(present_capacities):
  counts= {  
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }  #name the dict for convinience
  rated_cap=120 #assume

  for present_cap in present_capacities:
    soh=round((present_cap/rated_cap)*100)  #given formula
    if soh>80:
      counts["healthy"]+=1
    elif soh<=80 and soh>=62:
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
#making all efficient:upper boundry
  present_capacities = [120,120,120,120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 4)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")
#giving empty list:null
  present_capacities = []
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")

#giving float values:typecast
  present_capacities = [113.4, 116.12, 80.00, 95.1, 92, 70.3]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")

#all minimum health:lower boundry
  present_capacities = [0,0,0,0]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 4)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
