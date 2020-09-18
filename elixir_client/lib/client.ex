defmodule Client do
  def request(name) do
    greeter_service = System.get_env("GREETER_SERVICE", "localhost:50051")
    {:ok, channel} = GRPC.Stub.connect(greeter_service)
    request = Helloworld.HelloRequest.new(name: name)
    channel |> Helloworld.Greeter.Stub.say_hello(request)
  end
end
