from io import BytesIO
import torch
import torch.nn as nn

def copy_weights(src: nn.Module, dst: nn.Module) -> nn.Module:
    buf = BytesIO()
    torch.save(src.state_dict(), buf)
    buf.seek(0)
    dst.load_state_dict(torch.load(buf))