
def count_batteries_by_health(present_capacities):
  count_req= {  
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }  '''name the dict for convinience'''
  rated_cap=120 '''assume'''

  for present_cap in present_capacities:
    soh=(present_cap/rated_cap)*100  '''given formula'''
    if soh>80:
      count_req["healthy"]=cout_req["healthy"]+1
    elif soh<=80 and soh>=62:
      count_req["exchange"]=cout_req["exchange"]+1
    else:
      count_req["failed"]=cout_req["failed"]+1
  return count_req


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
