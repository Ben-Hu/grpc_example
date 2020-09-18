defmodule Mix.Tasks.Request do
  use Mix.Task

  def run(args) do
    Application.ensure_all_started(:client)
    args |> List.first() |> Client.request() |> IO.inspect()
  end
end
