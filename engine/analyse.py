from engine.greedy import analyse_position_greedy
from engine.minimax import analyse_position_minimax
from engine.alphabeta import analyse_position_alphabeta


def analyse_position(ui_board, turn):

    print("\n---- ANALYSIS ----\n")

    g_move, g_score, g_nodes, g_time = analyse_position_greedy(ui_board, turn)

    m_move, m_score, m_nodes, m_time = analyse_position_minimax(ui_board, turn)

    a_move, a_score, a_nodes, a_time = analyse_position_alphabeta(ui_board, turn)

    print("\n---- COMPARISON ----")

    print("\nGREEDY:")
    print("Move:", g_move, "| Score:", g_score)
    print("Nodes:", g_nodes, "| Time:", round(g_time, 5))

    print("\nMINIMAX:")
    print("Move:", m_move, "| Score:", m_score)
    print("Nodes:", m_nodes, "| Time:", round(m_time, 5))

    print("\nALPHA-BETA:")
    print("Move:", a_move, "| Score:", a_score)
    print("Nodes:", a_nodes, "| Time:", round(a_time, 5))

    print("\n-----------------\n")

    # RETURN (for UI)
    return {
        "greedy": {
            "move": g_move,
            "score": g_score,
            "nodes": g_nodes,
            "time": g_time
        },
        "minimax": {
            "move": m_move,
            "score": m_score,
            "nodes": m_nodes,
            "time": m_time
        },
        "alphabeta": {
            "move": a_move,
            "score": a_score,
            "nodes": a_nodes,
            "time": a_time
        }
    }