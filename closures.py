def print_with_memory():
  record = []

  def inner(data):
    print(data)
    record.append(data)
    print(record)
  return inner

print_ = print_with_memory()

print_("haha")
print_("hihi")