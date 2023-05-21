import pyshark
import matplotlib.pyplot as plt
import numpy as np

protocol_list = []
number_of_protocols = 100

def print_live_protocols_graph():
    capture = pyshark.LiveCapture("Wi-Fi")
    unique_protocols = []
    counts = []

    for packet in capture:
        protocol_list.append(packet.highest_layer)
        unique_protocols, counts = np.unique(protocol_list, return_counts=True)
        plt.style.use("seaborn-v0_8")
        plt.bar(unique_protocols, counts, align="center", color=["b", "g", "r", "c", "m"])
        plt.xlabel('Protocol Name')
        plt.ylabel('Frequency')
        plt.title('Live Protocol Graph - Captured: ' + str(len(protocol_list)))
        plt.tight_layout()
        plt.pause(0.1)

        if len(protocol_list) == number_of_protocols:
            plt.savefig("live-protocol-graph\Protocol_Graph.png")
            capture.close()
            return 0

    plt.show()

if __name__ == "__main__":
    print_live_protocols_graph()
