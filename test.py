def main():
  data = "something"
  # some comments
  env = StreamExecutionEnvironment.get_execution_environment()
  parr_num = 4
  env.set_parallelism(parr_num)
  t_env = StreamTableEnvironment.create(env)
  t_env.exec("method",data)
