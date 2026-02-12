from pyteal import *

def approval_program():
    
    reputation_key = Bytes("reputation")

    on_create = Seq(
        App.globalPut(reputation_key, Int(0)),
        Return(Int(1))
    )

    handle_update_reputation = Seq(
        App.globalPut(
            reputation_key,
            App.globalGet(reputation_key) + Int(1)
        ),
        Return(Int(1))
    )

    handle_read_reputation = Return(Int(1))

    program = Cond(
        [Txn.application_id() == Int(0), on_create],
        [Txn.application_args[0] == Bytes("update"), handle_update_reputation],
        [Txn.application_args[0] == Bytes("read"), handle_read_reputation],
    )

    return program


def clear_program():
    return Return(Int(1))


if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        f.write(compileTeal(approval_program(), Mode.Application, version=6))

    with open("clear.teal", "w") as f:
        f.write(compileTeal(clear_program(), Mode.Application, version=6))
