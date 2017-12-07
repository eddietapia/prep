/*
Modify and return the given map as follows: if the key "a" has a value, set the key "b" to have that same value. In all cases remove the key "c", leaving the rest of the map unchanged.


mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
*/
public Map<String, String> mapShare(Map<String, String> map) {
  Map<String, String> newMap = new HashMap<String, String>();
  String newValue = map.get("a");

  for (Map.Entry<String, String> entry: map.entrySet()){
    String key = entry.getKey();

    if ( !key.equals("c")){
      newMap.put(key, entry.getValue());
    }
  }
  if (newValue != null){
        newMap.put("b", newValue);
  }
  return newMap;
  
}
