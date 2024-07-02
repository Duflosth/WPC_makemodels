def WPC_test_orientation_tree(x):
  if x[22] <= 4.76:
    if x[22] <= -4.35:
      if x[34] <= -4.18:
        if x[29] <= -8.31:
          if x[28] <= -6.24:
            if x[24] <= 1.23:
              if x[25] <= 0.91:
                return 1
              else:  # if x[25] > 0.91
                return 2
            else:  # if x[24] > 1.23
              return 3
          else:  # if x[28] > -6.24
            if x[16] <= -6.54:
              if x[28] <= -4.36:
                return 1
              else:  # if x[28] > -4.36
                return 3
            else:  # if x[16] > -6.54
              return 3
        else:  # if x[29] > -8.31
          if x[6] <= 4.57:
            if x[35] <= 7.37:
              if x[29] <= 182.5:
                if x[37] <= -3.72:
                  return 0
                else:  # if x[37] > -3.72
                  if x[28] <= -0.72:
                    if x[14] <= -4.34:
                      if x[21] <= -10.32:
                        return 0
                      else:  # if x[21] > -10.32
                        return 1
                    else:  # if x[14] > -4.34
                      if x[28] <= -4.13:
                        return 1
                      else:  # if x[28] > -4.13
                        if x[36] <= 0.85:
                          return 1
                        else:  # if x[36] > 0.85
                          return 2
                  else:  # if x[28] > -0.72
                    return 2
              else:  # if x[29] > 182.5
                if x[24] <= -1.18:
                  return 3
                else:  # if x[24] > -1.18
                  return 1
            else:  # if x[35] > 7.37
              if x[28] <= -5.38:
                if x[37] <= -0.84:
                  if x[13] <= 0.7:
                    if x[23] <= 8.26:
                      return 1
                    else:  # if x[23] > 8.26
                      return 3
                  else:  # if x[13] > 0.7
                    return 2
                else:  # if x[37] > -0.84
                  if x[13] <= -1.17:
                    return 3
                  else:  # if x[13] > -1.17
                    return 1
              else:  # if x[28] > -5.38
                if x[4] <= -5.71:
                  return 1
                else:  # if x[4] > -5.71
                  return 3
          else:  # if x[6] > 4.57
            return 0
      else:  # if x[34] > -4.18
        if x[10] <= -3.9:
          if x[11] <= -7.73:
            if x[29] <= -2.48:
              if x[27] <= -11.19:
                if x[31] <= -0.21:
                  return 1
                else:  # if x[31] > -0.21
                  return 2
              else:  # if x[27] > -11.19
                return 3
            else:  # if x[29] > -2.48
              if x[23] <= -5.97:
                if x[1] <= 0.84:
                  return 2
                else:  # if x[1] > 0.84
                  return 3
              else:  # if x[23] > -5.97
                if x[6] <= -2.8:
                  return 0
                else:  # if x[6] > -2.8
                  return 1
          else:  # if x[11] > -7.73
            if x[11] <= 7.69:
              if x[12] <= 4.53:
                if x[13] <= -3.34:
                  return 2
                else:  # if x[13] > -3.34
                  if x[32] <= -3.54:
                    return 0
                  else:  # if x[32] > -3.54
                    if x[23] <= 301.01:
                      if x[11] <= 6.16:
                        if x[37] <= -1.68:
                          if x[6] <= -0.29:
                            return 2
                          else:  # if x[6] > -0.29
                            return 1
                        else:  # if x[37] > -1.68
                          if x[31] <= -1.65:
                            if x[9] <= -0.97:
                              return 3
                            else:  # if x[9] > -0.97
                              return 1
                          else:  # if x[31] > -1.65
                            return 1
                      else:  # if x[11] > 6.16
                        if x[0] <= 0.18:
                          return 1
                        else:  # if x[0] > 0.18
                          return 3
                    else:  # if x[23] > 301.01
                      return 2
              else:  # if x[12] > 4.53
                return 0
            else:  # if x[11] > 7.69
              if x[9] <= -5.0:
                if x[37] <= -0.9:
                  return 2
                else:  # if x[37] > -0.9
                  if x[31] <= 1.81:
                    return 1
                  else:  # if x[31] > 1.81
                    return 0
              else:  # if x[9] > -5.0
                return 3
        else:  # if x[10] > -3.9
          if x[33] <= 6.01:
            if x[33] <= -6.78:
              if x[10] <= 5.46:
                if x[30] <= -1.21:
                  if x[5] <= -4.29:
                    return 3
                  else:  # if x[5] > -4.29
                    if x[22] <= -12.83:
                      return 1
                    else:  # if x[22] > -12.83
                      return 0
                else:  # if x[30] > -1.21
                  if x[35] <= -109.91:
                    return 1
                  else:  # if x[35] > -109.91
                    if x[2] <= -1.68:
                      if x[1] <= -0.07:
                        return 2
                      else:  # if x[1] > -0.07
                        return 0
                    else:  # if x[2] > -1.68
                      return 2
              else:  # if x[10] > 5.46
                if x[34] <= -2.93:
                  return 2
                else:  # if x[34] > -2.93
                  return 1
            else:  # if x[33] > -6.78
              if x[10] <= 8.99:
                if x[9] <= -7.12:
                  if x[36] <= 0.02:
                    if x[24] <= -1.49:
                      if x[28] <= -1.43:
                        return 0
                      else:  # if x[28] > -1.43
                        return 3
                    else:  # if x[24] > -1.49
                      return 2
                  else:  # if x[36] > 0.02
                    if x[0] <= -1.28:
                      if x[15] <= -46.83:
                        return 1
                      else:  # if x[15] > -46.83
                        return 0
                    else:  # if x[0] > -1.28
                      return 1
                else:  # if x[9] > -7.12
                  if x[3] <= 7.28:
                    if x[1] <= 1.33:
                      if x[29] <= -85.69:
                        return 1
                      else:  # if x[29] > -85.69
                        if x[4] <= -3.49:
                          if x[35] <= 0.56:
                            if x[24] <= 1.02:
                              return 1
                            else:  # if x[24] > 1.02
                              return 3
                          else:  # if x[35] > 0.56
                            return 3
                        else:  # if x[4] > -3.49
                          if x[21] <= 10.33:
                            if x[15] <= 60.37:
                              if x[23] <= -195.2:
                                return 2
                              else:  # if x[23] > -195.2
                                if x[13] <= 4.55:
                                  if x[36] <= -4.44:
                                    return 0
                                  else:  # if x[36] > -4.44
                                    if x[37] <= -4.25:
                                      return 0
                                    else:  # if x[37] > -4.25
                                      if x[40] <= -3.51:
                                        if x[10] <= -2.52:
                                          return 1
                                        else:  # if x[10] > -2.52
                                          if x[40] <= -3.57:
                                            if x[26] <= -0.35:
                                              if x[30] <= -1.24:
                                                return 3
                                              else:  # if x[30] > -1.24
                                                return 1
                                            else:  # if x[26] > -0.35
                                              return 3
                                          else:  # if x[40] > -3.57
                                            return 1
                                      else:  # if x[40] > -3.51
                                        return 3
                                else:  # if x[13] > 4.55
                                  return 0
                            else:  # if x[15] > 60.37
                              return 0
                          else:  # if x[21] > 10.33
                            if x[17] <= 1.87:
                              return 2
                            else:  # if x[17] > 1.87
                              if x[3] <= -3.18:
                                return 0
                              else:  # if x[3] > -3.18
                                return 3
                    else:  # if x[1] > 1.33
                      if x[11] <= -4.42:
                        return 3
                      else:  # if x[11] > -4.42
                        if x[11] <= 6.57:
                          return 0
                        else:  # if x[11] > 6.57
                          return 3
                  else:  # if x[3] > 7.28
                    if x[5] <= -4.77:
                      if x[14] <= 0.3:
                        return 0
                      else:  # if x[14] > 0.3
                        return 1
                    else:  # if x[5] > -4.77
                      return 2
              else:  # if x[10] > 8.99
                if x[36] <= 3.04:
                  return 1
                else:  # if x[36] > 3.04
                  return 3
          else:  # if x[33] > 6.01
            if x[40] <= 7.91:
              if x[0] <= 0.52:
                return 2
              else:  # if x[0] > 0.52
                if x[1] <= -0.88:
                  return 2
                else:  # if x[1] > -0.88
                  if x[39] <= 16.33:
                    if x[19] <= 1.14:
                      return 0
                    else:  # if x[19] > 1.14
                      return 3
                  else:  # if x[39] > 16.33
                    return 1
            else:  # if x[40] > 7.91
              if x[19] <= -1.47:
                return 2
              else:  # if x[19] > -1.47
                return 1
    else:  # if x[22] > -4.35
      if x[21] <= 4.64:
        if x[21] <= -4.61:
          if x[23] <= 4.18:
            if x[23] <= -5.28:
              if x[21] <= -7.15:
                if x[4] <= -2.94:
                  if x[33] <= -1.48:
                    if x[20] <= -0.54:
                      if x[30] <= -0.04:
                        return 2
                      else:  # if x[30] > -0.04
                        if x[3] <= -2.44:
                          return 3
                        else:  # if x[3] > -2.44
                          return 1
                    else:  # if x[20] > -0.54
                      if x[26] <= 1.28:
                        if x[1] <= -1.04:
                          return 2
                        else:  # if x[1] > -1.04
                          return 1
                      else:  # if x[26] > 1.28
                        return 3
                  else:  # if x[33] > -1.48
                    if x[23] <= -91.08:
                      if x[20] <= -1.68:
                        return 0
                      else:  # if x[20] > -1.68
                        return 1
                    else:  # if x[23] > -91.08
                      if x[21] <= -350.08:
                        return 3
                      else:  # if x[21] > -350.08
                        return 2
                else:  # if x[4] > -2.94
                  if x[11] <= -4.91:
                    if x[15] <= -23.66:
                      if x[25] <= -0.57:
                        return 2
                      else:  # if x[25] > -0.57
                        if x[41] <= -0.71:
                          return 1
                        else:  # if x[41] > -0.71
                          return 3
                    else:  # if x[15] > -23.66
                      if x[31] <= -0.47:
                        if x[12] <= -0.4:
                          if x[24] <= -0.02:
                            if x[16] <= 1.09:
                              return 2
                            else:  # if x[16] > 1.09
                              return 1
                          else:  # if x[24] > -0.02
                            return 3
                        else:  # if x[12] > -0.4
                          return 1
                      else:  # if x[31] > -0.47
                        if x[15] <= 12.99:
                          if x[35] <= -15.79:
                            return 1
                          else:  # if x[35] > -15.79
                            if x[22] <= 1.77:
                              return 3
                            else:  # if x[22] > 1.77
                              return 1
                        else:  # if x[15] > 12.99
                          if x[1] <= 0.88:
                            return 0
                          else:  # if x[1] > 0.88
                            return 3
                  else:  # if x[11] > -4.91
                    if x[34] <= -7.33:
                      return 1
                    else:  # if x[34] > -7.33
                      if x[21] <= -228.64:
                        return 3
                      else:  # if x[21] > -228.64
                        if x[21] <= -8.78:
                          if x[17] <= 12.83:
                            if x[41] <= -15.42:
                              if x[10] <= -1.49:
                                return 2
                              else:  # if x[10] > -1.49
                                if x[35] <= -24.7:
                                  return 1
                                else:  # if x[35] > -24.7
                                  return 3
                            else:  # if x[41] > -15.42
                              if x[10] <= 0.32:
                                return 2
                              else:  # if x[10] > 0.32
                                if x[10] <= 0.63:
                                  return 3
                                else:  # if x[10] > 0.63
                                  return 2
                          else:  # if x[17] > 12.83
                            if x[21] <= -32.58:
                              return 2
                            else:  # if x[21] > -32.58
                              if x[40] <= -3.62:
                                return 1
                              else:  # if x[40] > -3.62
                                return 0
                        else:  # if x[21] > -8.78
                          if x[4] <= -0.61:
                            return 3
                          else:  # if x[4] > -0.61
                            if x[2] <= 3.89:
                              return 2
                            else:  # if x[2] > 3.89
                              return 0
              else:  # if x[21] > -7.15
                if x[39] <= -6.15:
                  if x[22] <= -1.14:
                    return 1
                  else:  # if x[22] > -1.14
                    if x[22] <= 1.57:
                      return 2
                    else:  # if x[22] > 1.57
                      return 0
                else:  # if x[39] > -6.15
                  if x[34] <= 8.91:
                    if x[15] <= -8.75:
                      return 1
                    else:  # if x[15] > -8.75
                      return 3
                  else:  # if x[34] > 8.91
                    return 1
            else:  # if x[23] > -5.28
              if x[1] <= -3.87:
                if x[7] <= -1.07:
                  return 0
                else:  # if x[7] > -1.07
                  if x[4] <= -1.19:
                    return 3
                  else:  # if x[4] > -1.19
                    return 2
              else:  # if x[1] > -3.87
                if x[21] <= -355.53:
                  if x[22] <= 1.84:
                    if x[39] <= 4.98:
                      return 3
                    else:  # if x[39] > 4.98
                      if x[25] <= -0.48:
                        return 2
                      else:  # if x[25] > -0.48
                        return 1
                  else:  # if x[22] > 1.84
                    return 1
                else:  # if x[21] > -355.53
                  if x[18] <= 3.14:
                    if x[1] <= 4.82:
                      if x[21] <= -5.98:
                        if x[26] <= -5.64:
                          if x[25] <= -0.12:
                            return 0
                          else:  # if x[25] > -0.12
                            return 2
                        else:  # if x[26] > -5.64
                          if x[6] <= -4.3:
                            return 3
                          else:  # if x[6] > -4.3
                            if x[0] <= -3.98:
                              return 3
                            else:  # if x[0] > -3.98
                              if x[7] <= -4.11:
                                return 0
                              else:  # if x[7] > -4.11
                                if x[7] <= 4.18:
                                  if x[41] <= 351.9:
                                    if x[28] <= -10.32:
                                      if x[13] <= -0.57:
                                        return 2
                                      else:  # if x[13] > -0.57
                                        return 3
                                    else:  # if x[28] > -10.32
                                      if x[23] <= -4.82:
                                        if x[40] <= 3.05:
                                          return 2
                                        else:  # if x[40] > 3.05
                                          return 1
                                      else:  # if x[23] > -4.82
                                        if x[29] <= 7.52:
                                          return 2
                                        else:  # if x[29] > 7.52
                                          if x[1] <= -2.13:
                                            return 0
                                          else:  # if x[1] > -2.13
                                            return 2
                                  else:  # if x[41] > 351.9
                                    if x[3] <= -5.06:
                                      return 2
                                    else:  # if x[3] > -5.06
                                      return 3
                                else:  # if x[7] > 4.18
                                  return 0
                      else:  # if x[21] > -5.98
                        if x[29] <= 3.42:
                          if x[23] <= -1.96:
                            if x[20] <= 0.34:
                              if x[8] <= 0.49:
                                if x[35] <= -0.97:
                                  return 1
                                else:  # if x[35] > -0.97
                                  return 2
                              else:  # if x[8] > 0.49
                                return 2
                            else:  # if x[20] > 0.34
                              if x[19] <= 0.09:
                                return 3
                              else:  # if x[19] > 0.09
                                return 1
                          else:  # if x[23] > -1.96
                            if x[20] <= -2.95:
                              if x[8] <= -4.89:
                                return 1
                              else:  # if x[8] > -4.89
                                return 0
                            else:  # if x[20] > -2.95
                              if x[5] <= -6.22:
                                if x[25] <= -0.73:
                                  return 2
                                else:  # if x[25] > -0.73
                                  if x[21] <= -4.95:
                                    return 0
                                  else:  # if x[21] > -4.95
                                    return 3
                              else:  # if x[5] > -6.22
                                if x[7] <= 2.41:
                                  if x[10] <= -6.32:
                                    return 3
                                  else:  # if x[10] > -6.32
                                    return 2
                                else:  # if x[7] > 2.41
                                  return 0
                        else:  # if x[29] > 3.42
                          if x[7] <= 0.65:
                            return 0
                          else:  # if x[7] > 0.65
                            if x[2] <= 1.41:
                              return 2
                            else:  # if x[2] > 1.41
                              return 3
                    else:  # if x[1] > 4.82
                      return 0
                  else:  # if x[18] > 3.14
                    return 0
          else:  # if x[23] > 4.18
            if x[23] <= 226.55:
              if x[4] <= 2.51:
                if x[21] <= -216.22:
                  if x[15] <= 9.86:
                    return 3
                  else:  # if x[15] > 9.86
                    if x[28] <= 5.39:
                      return 2
                    else:  # if x[28] > 5.39
                      return 1
                else:  # if x[21] > -216.22
                  if x[21] <= -6.36:
                    if x[23] <= 6.6:
                      if x[21] <= -10.74:
                        if x[5] <= 7.26:
                          return 2
                        else:  # if x[5] > 7.26
                          return 0
                      else:  # if x[21] > -10.74
                        if x[14] <= 0.8:
                          if x[20] <= 1.04:
                            return 0
                          else:  # if x[20] > 1.04
                            return 2
                        else:  # if x[14] > 0.8
                          if x[4] <= -0.11:
                            return 0
                          else:  # if x[4] > -0.11
                            return 2
                    else:  # if x[23] > 6.6
                      if x[28] <= -3.72:
                        if x[39] <= -1.72:
                          if x[29] <= 9.14:
                            return 2
                          else:  # if x[29] > 9.14
                            if x[19] <= -0.26:
                              if x[24] <= -0.61:
                                return 0
                              else:  # if x[24] > -0.61
                                return 3
                            else:  # if x[19] > -0.26
                              return 1
                        else:  # if x[39] > -1.72
                          if x[40] <= -5.04:
                            return 1
                          else:  # if x[40] > -5.04
                            return 0
                      else:  # if x[28] > -3.72
                        if x[28] <= 4.4:
                          if x[15] <= -83.72:
                            if x[25] <= 0.11:
                              return 2
                            else:  # if x[25] > 0.11
                              return 0
                          else:  # if x[15] > -83.72
                            if x[22] <= -3.62:
                              if x[40] <= -1.21:
                                if x[10] <= 0.45:
                                  return 3
                                else:  # if x[10] > 0.45
                                  return 2
                              else:  # if x[40] > -1.21
                                return 0
                            else:  # if x[22] > -3.62
                              if x[10] <= -5.03:
                                if x[4] <= -1.32:
                                  return 0
                                else:  # if x[4] > -1.32
                                  return 3
                              else:  # if x[10] > -5.03
                                return 0
                        else:  # if x[28] > 4.4
                          if x[6] <= 1.01:
                            return 1
                          else:  # if x[6] > 1.01
                            if x[11] <= -1.88:
                              return 3
                            else:  # if x[11] > -1.88
                              return 0
                  else:  # if x[21] > -6.36
                    if x[23] <= 11.41:
                      if x[26] <= -0.09:
                        if x[40] <= -3.38:
                          if x[7] <= -2.39:
                            return 0
                          else:  # if x[7] > -2.39
                            return 3
                        else:  # if x[40] > -3.38
                          if x[16] <= -7.18:
                            return 1
                          else:  # if x[16] > -7.18
                            return 0
                      else:  # if x[26] > -0.09
                        if x[7] <= -0.94:
                          return 2
                        else:  # if x[7] > -0.94
                          if x[13] <= -0.04:
                            if x[35] <= -0.59:
                              return 2
                            else:  # if x[35] > -0.59
                              if x[23] <= 7.43:
                                if x[3] <= 0.4:
                                  return 1
                                else:  # if x[3] > 0.4
                                  return 0
                              else:  # if x[23] > 7.43
                                return 3
                          else:  # if x[13] > -0.04
                            if x[3] <= 165.87:
                              return 0
                            else:  # if x[3] > 165.87
                              return 1
                    else:  # if x[23] > 11.41
                      return 3
              else:  # if x[4] > 2.51
                if x[8] <= -0.26:
                  if x[28] <= 3.33:
                    if x[11] <= -198.35:
                      return 1
                    else:  # if x[11] > -198.35
                      return 0
                  else:  # if x[28] > 3.33
                    if x[28] <= 3.38:
                      return 1
                    else:  # if x[28] > 3.38
                      return 3
                else:  # if x[8] > -0.26
                  if x[39] <= -4.46:
                    if x[11] <= 4.57:
                      if x[11] <= 0.92:
                        if x[22] <= -0.96:
                          if x[1] <= 0.4:
                            return 0
                          else:  # if x[1] > 0.4
                            return 3
                        else:  # if x[22] > -0.96
                          return 1
                      else:  # if x[11] > 0.92
                        return 2
                    else:  # if x[11] > 4.57
                      if x[12] <= -1.69:
                        return 0
                      else:  # if x[12] > -1.69
                        return 1
                  else:  # if x[39] > -4.46
                    if x[40] <= -2.59:
                      if x[25] <= -1.75:
                        if x[8] <= 0.42:
                          return 3
                        else:  # if x[8] > 0.42
                          return 0
                      else:  # if x[25] > -1.75
                        return 1
                    else:  # if x[40] > -2.59
                      if x[33] <= -14.03:
                        if x[5] <= -0.54:
                          return 0
                        else:  # if x[5] > -0.54
                          if x[19] <= 1.28:
                            return 1
                          else:  # if x[19] > 1.28
                            return 2
                      else:  # if x[33] > -14.03
                        if x[23] <= 5.72:
                          return 1
                        else:  # if x[23] > 5.72
                          return 3
            else:  # if x[23] > 226.55
              if x[21] <= -14.1:
                if x[21] <= -236.52:
                  if x[7] <= -0.22:
                    return 3
                  else:  # if x[7] > -0.22
                    return 0
                else:  # if x[21] > -236.52
                  if x[4] <= -6.96:
                    return 1
                  else:  # if x[4] > -6.96
                    return 2
              else:  # if x[21] > -14.1
                if x[13] <= -0.55:
                  return 2
                else:  # if x[13] > -0.55
                  return 3
        else:  # if x[21] > -4.61
          if x[23] <= 4.7:
            if x[23] <= -2.42:
              if x[38] <= -2.75:
                if x[5] <= 12.26:
                  if x[32] <= 1.62:
                    return 0
                  else:  # if x[32] > 1.62
                    return 1
                else:  # if x[5] > 12.26
                  if x[1] <= -0.08:
                    return 0
                  else:  # if x[1] > -0.08
                    return 3
              else:  # if x[38] > -2.75
                if x[0] <= -4.1:
                  if x[17] <= -12.33:
                    return 3
                  else:  # if x[17] > -12.33
                    if x[18] <= 2.11:
                      return 0
                    else:  # if x[18] > 2.11
                      return 3
                else:  # if x[0] > -4.1
                  if x[33] <= 5.76:
                    if x[14] <= 2.61:
                      if x[3] <= 7.17:
                        if x[18] <= -6.97:
                          if x[9] <= 177.39:
                            return 0
                          else:  # if x[9] > 177.39
                            return 3
                        else:  # if x[18] > -6.97
                          if x[29] <= -2.8:
                            if x[34] <= 5.09:
                              if x[1] <= 3.5:
                                if x[39] <= 6.73:
                                  if x[2] <= 3.5:
                                    if x[21] <= 3.62:
                                      if x[26] <= 5.94:
                                        if x[3] <= -16.32:
                                          if x[5] <= -26.52:
                                            return 1
                                          else:  # if x[5] > -26.52
                                            if x[40] <= 4.6:
                                              return 3
                                            else:  # if x[40] > 4.6
                                              return 2
                                        else:  # if x[3] > -16.32
                                          if x[39] <= -7.54:
                                            if x[4] <= -4.48:
                                              return 1
                                            else:  # if x[4] > -4.48
                                              return 3
                                          else:  # if x[39] > -7.54
                                            if x[40] <= -10.77:
                                              return 1
                                            else:  # if x[40] > -10.77
                                              if x[20] <= -2.67:
                                                if x[16] <= -0.0:
                                                  return 2
                                                else:  # if x[16] > -0.0
                                                  return 3
                                              else:  # if x[20] > -2.67
                                                if x[5] <= 356.08:
                                                  if x[8] <= 3.63:
                                                    if x[14] <= -2.09:
                                                      if x[9] <= 2.68:
                                                        return 3
                                                      else:  # if x[9] > 2.68
                                                        return 2
                                                    else:  # if x[14] > -2.09
                                                      if x[38] <= -1.71:
                                                        if x[31] <= -0.93:
                                                          if x[0] <= 1.48:
                                                            return 0
                                                          else:  # if x[0] > 1.48
                                                            return 3
                                                        else:  # if x[31] > -0.93
                                                          return 3
                                                      else:  # if x[38] > -1.71
                                                        if x[0] <= -2.42:
                                                          if x[23] <= -4.55:
                                                            return 3
                                                          else:  # if x[23] > -4.55
                                                            if x[6] <= -0.55:
                                                              return 0
                                                            else:  # if x[6] > -0.55
                                                              return 3
                                                        else:  # if x[0] > -2.42
                                                          if x[8] <= -2.66:
                                                            if x[8] <= -2.75:
                                                              return 3
                                                            else:  # if x[8] > -2.75
                                                              return 2
                                                          else:  # if x[8] > -2.66
                                                            if x[40] <= -5.94:
                                                              if x[29] <= -5.44:
                                                                return 3
                                                              else:  # if x[29] > -5.44
                                                                if x[15] <= -0.19:
                                                                  return 2
                                                                else:  # if x[15] > -0.19
                                                                  return 1
                                                            else:  # if x[40] > -5.94
                                                              if x[33] <= 5.39:
                                                                if x[22] <= -4.22:
                                                                  if x[0] <= 0.32:
                                                                    return 1
                                                                  else:  # if x[0] > 0.32
                                                                    return 3
                                                                else:  # if x[22] > -4.22
                                                                  if x[3] <= -7.94:
                                                                    if x[21] <= 2.1:
                                                                      return 3
                                                                    else:  # if x[21] > 2.1
                                                                      return 0
                                                                  else:  # if x[3] > -7.94
                                                                    if x[29] <= -3.63:
                                                                      return 3
                                                                    else:  # if x[29] > -3.63
                                                                      if x[29] <= -3.62:
                                                                        return 0
                                                                      else:  # if x[29] > -3.62
                                                                        if x[34] <= -4.93:
                                                                          return 1
                                                                        else:  # if x[34] > -4.93
                                                                          if x[21] <= -3.7:
                                                                            return 1
                                                                          else:  # if x[21] > -3.7
                                                                            if x[28] <= 3.2:
                                                                              if x[38] <= -1.16:
                                                                                if x[27] <= -2.5:
                                                                                  return 0
                                                                                else:  # if x[27] > -2.5
                                                                                  return 3
                                                                              else:  # if x[38] > -1.16
                                                                                return 3
                                                                            else:  # if x[28] > 3.2
                                                                              if x[36] <= 0.22:
                                                                                return 3
                                                                              else:  # if x[36] > 0.22
                                                                                return 1
                                                              else:  # if x[33] > 5.39
                                                                if x[32] <= 1.13:
                                                                  return 3
                                                                else:  # if x[32] > 1.13
                                                                  return 0
                                                  else:  # if x[8] > 3.63
                                                    if x[7] <= -0.06:
                                                      return 0
                                                    else:  # if x[7] > -0.06
                                                      return 3
                                                else:  # if x[5] > 356.08
                                                  if x[35] <= -3.82:
                                                    return 3
                                                  else:  # if x[35] > -3.82
                                                    return 1
                                      else:  # if x[26] > 5.94
                                        return 0
                                    else:  # if x[21] > 3.62
                                      if x[5] <= -1.45:
                                        return 3
                                      else:  # if x[5] > -1.45
                                        if x[5] <= 5.65:
                                          if x[2] <= -1.87:
                                            return 0
                                          else:  # if x[2] > -1.87
                                            return 2
                                        else:  # if x[5] > 5.65
                                          if x[10] <= 1.59:
                                            return 3
                                          else:  # if x[10] > 1.59
                                            return 1
                                  else:  # if x[2] > 3.5
                                    if x[33] <= -2.47:
                                      return 3
                                    else:  # if x[33] > -2.47
                                      return 0
                                else:  # if x[39] > 6.73
                                  if x[2] <= -0.25:
                                    return 0
                                  else:  # if x[2] > -0.25
                                    if x[22] <= -2.26:
                                      return 2
                                    else:  # if x[22] > -2.26
                                      return 3
                              else:  # if x[1] > 3.5
                                if x[10] <= -4.87:
                                  return 3
                                else:  # if x[10] > -4.87
                                  return 0
                            else:  # if x[34] > 5.09
                              if x[41] <= -4.21:
                                return 3
                              else:  # if x[41] > -4.21
                                if x[27] <= -1.1:
                                  if x[25] <= -1.28:
                                    return 2
                                  else:  # if x[25] > -1.28
                                    return 1
                                else:  # if x[27] > -1.1
                                  if x[4] <= -2.78:
                                    return 2
                                  else:  # if x[4] > -2.78
                                    return 3
                          else:  # if x[29] > -2.8
                            if x[28] <= 2.44:
                              if x[4] <= 8.88:
                                if x[11] <= -3.08:
                                  if x[13] <= 3.78:
                                    if x[12] <= -2.76:
                                      if x[5] <= -4.08:
                                        return 0
                                      else:  # if x[5] > -4.08
                                        return 1
                                    else:  # if x[12] > -2.76
                                      if x[26] <= 2.5:
                                        if x[7] <= -7.58:
                                          return 0
                                        else:  # if x[7] > -7.58
                                          if x[20] <= -2.78:
                                            return 0
                                          else:  # if x[20] > -2.78
                                            if x[2] <= 3.36:
                                              if x[32] <= -2.85:
                                                return 0
                                              else:  # if x[32] > -2.85
                                                if x[28] <= -4.38:
                                                  if x[40] <= -0.8:
                                                    return 1
                                                  else:  # if x[40] > -0.8
                                                    return 3
                                                else:  # if x[28] > -4.38
                                                  if x[2] <= -3.56:
                                                    if x[30] <= 0.6:
                                                      return 0
                                                    else:  # if x[30] > 0.6
                                                      return 3
                                                  else:  # if x[2] > -3.56
                                                    if x[38] <= -1.23:
                                                      if x[17] <= -4.6:
                                                        return 3
                                                      else:  # if x[17] > -4.6
                                                        return 0
                                                    else:  # if x[38] > -1.23
                                                      return 3
                                            else:  # if x[2] > 3.36
                                              return 0
                                      else:  # if x[26] > 2.5
                                        if x[10] <= -0.37:
                                          if x[8] <= -1.38:
                                            return 0
                                          else:  # if x[8] > -1.38
                                            return 3
                                        else:  # if x[10] > -0.37
                                          return 2
                                  else:  # if x[13] > 3.78
                                    return 0
                                else:  # if x[11] > -3.08
                                  if x[26] <= 1.25:
                                    if x[32] <= -0.02:
                                      if x[38] <= 0.31:
                                        if x[16] <= -3.33:
                                          return 1
                                        else:  # if x[16] > -3.33
                                          if x[40] <= 3.3:
                                            return 0
                                          else:  # if x[40] > 3.3
                                            return 3
                                      else:  # if x[38] > 0.31
                                        if x[19] <= 2.27:
                                          if x[14] <= 1.11:
                                            return 3
                                          else:  # if x[14] > 1.11
                                            return 1
                                        else:  # if x[19] > 2.27
                                          return 0
                                    else:  # if x[32] > -0.02
                                      if x[28] <= -1.72:
                                        if x[7] <= 0.19:
                                          return 1
                                        else:  # if x[7] > 0.19
                                          return 0
                                      else:  # if x[28] > -1.72
                                        if x[36] <= 2.01:
                                          if x[18] <= -4.24:
                                            return 0
                                          else:  # if x[18] > -4.24
                                            if x[15] <= 5.65:
                                              if x[17] <= 356.61:
                                                if x[5] <= -187.29:
                                                  return 1
                                                else:  # if x[5] > -187.29
                                                  return 3
                                              else:  # if x[17] > 356.61
                                                return 1
                                            else:  # if x[15] > 5.65
                                              return 0
                                        else:  # if x[36] > 2.01
                                          return 0
                                  else:  # if x[26] > 1.25
                                    if x[29] <= 5.4:
                                      if x[4] <= 2.31:
                                        return 0
                                      else:  # if x[4] > 2.31
                                        return 1
                                    else:  # if x[29] > 5.4
                                      if x[19] <= -0.12:
                                        return 2
                                      else:  # if x[19] > -0.12
                                        return 3
                              else:  # if x[4] > 8.88
                                return 1
                            else:  # if x[28] > 2.44
                              if x[40] <= 4.08:
                                if x[28] <= 2.96:
                                  if x[10] <= 1.47:
                                    if x[7] <= -2.9:
                                      return 3
                                    else:  # if x[7] > -2.9
                                      return 0
                                  else:  # if x[10] > 1.47
                                    return 1
                                else:  # if x[28] > 2.96
                                  if x[34] <= 1.09:
                                    return 0
                                  else:  # if x[34] > 1.09
                                    if x[29] <= -2.71:
                                      return 1
                                    else:  # if x[29] > -2.71
                                      if x[4] <= -1.09:
                                        return 1
                                      else:  # if x[4] > -1.09
                                        return 3
                              else:  # if x[40] > 4.08
                                return 1
                      else:  # if x[3] > 7.17
                        if x[3] <= 353.04:
                          if x[40] <= -3.26:
                            return 1
                          else:  # if x[40] > -3.26
                            if x[40] <= 3.41:
                              if x[4] <= -6.66:
                                return 3
                              else:  # if x[4] > -6.66
                                return 0
                            else:  # if x[40] > 3.41
                              if x[25] <= -0.35:
                                return 2
                              else:  # if x[25] > -0.35
                                if x[17] <= -10.68:
                                  return 3
                                else:  # if x[17] > -10.68
                                  return 1
                        else:  # if x[3] > 353.04
                          return 3
                    else:  # if x[14] > 2.61
                      if x[8] <= 1.83:
                        if x[32] <= 0.3:
                          if x[13] <= -5.37:
                            return 0
                          else:  # if x[13] > -5.37
                            return 3
                        else:  # if x[32] > 0.3
                          if x[28] <= -1.94:
                            return 1
                          else:  # if x[28] > -1.94
                            if x[15] <= -8.3:
                              return 3
                            else:  # if x[15] > -8.3
                              return 0
                      else:  # if x[8] > 1.83
                        return 0
                  else:  # if x[33] > 5.76
                    if x[21] <= 1.61:
                      if x[39] <= 6.45:
                        if x[19] <= 1.39:
                          if x[3] <= 15.64:
                            return 3
                          else:  # if x[3] > 15.64
                            return 1
                        else:  # if x[19] > 1.39
                          return 0
                      else:  # if x[39] > 6.45
                        if x[29] <= -6.64:
                          if x[16] <= -7.27:
                            return 1
                          else:  # if x[16] > -7.27
                            return 0
                        else:  # if x[29] > -6.64
                          if x[17] <= -13.72:
                            return 3
                          else:  # if x[17] > -13.72
                            return 2
                    else:  # if x[21] > 1.61
                      if x[35] <= -3.46:
                        if x[10] <= 3.24:
                          if x[37] <= -1.11:
                            return 3
                          else:  # if x[37] > -1.11
                            if x[39] <= 53.13:
                              return 0
                            else:  # if x[39] > 53.13
                              if x[23] <= -3.35:
                                return 2
                              else:  # if x[23] > -3.35
                                return 1
                        else:  # if x[10] > 3.24
                          if x[21] <= 3.59:
                            if x[27] <= 38.42:
                              return 1
                            else:  # if x[27] > 38.42
                              return 2
                          else:  # if x[21] > 3.59
                            return 3
                      else:  # if x[35] > -3.46
                        if x[41] <= 4.37:
                          return 2
                        else:  # if x[41] > 4.37
                          if x[31] <= 1.73:
                            return 3
                          else:  # if x[31] > 1.73
                            return 0
            else:  # if x[23] > -2.42
              if x[40] <= 3.0:
                if x[40] <= -3.52:
                  if x[24] <= 1.04:
                    if x[35] <= 5.31:
                      if x[41] <= -6.52:
                        if x[4] <= 3.0:
                          if x[25] <= -0.04:
                            if x[28] <= 2.34:
                              return 1
                            else:  # if x[28] > 2.34
                              if x[22] <= 1.87:
                                return 0
                              else:  # if x[22] > 1.87
                                return 3
                          else:  # if x[25] > -0.04
                            return 2
                        else:  # if x[4] > 3.0
                          if x[3] <= -26.4:
                            return 1
                          else:  # if x[3] > -26.4
                            return 3
                      else:  # if x[41] > -6.52
                        if x[39] <= 8.05:
                          if x[1] <= 1.86:
                            if x[39] <= -8.91:
                              if x[20] <= -0.15:
                                return 1
                              else:  # if x[20] > -0.15
                                return 2
                            else:  # if x[39] > -8.91
                              if x[0] <= -2.73:
                                return 0
                              else:  # if x[0] > -2.73
                                if x[25] <= -1.94:
                                  return 3
                                else:  # if x[25] > -1.94
                                  if x[38] <= 2.7:
                                    if x[31] <= -1.95:
                                      return 3
                                    else:  # if x[31] > -1.95
                                      if x[34] <= -2.38:
                                        if x[35] <= -6.27:
                                          if x[39] <= -1.38:
                                            return 3
                                          else:  # if x[39] > -1.38
                                            return 1
                                        else:  # if x[35] > -6.27
                                          return 1
                                      else:  # if x[34] > -2.38
                                        if x[27] <= -0.64:
                                          if x[10] <= -4.9:
                                            return 1
                                          else:  # if x[10] > -4.9
                                            return 3
                                        else:  # if x[27] > -0.64
                                          return 1
                                  else:  # if x[38] > 2.7
                                    return 3
                          else:  # if x[1] > 1.86
                            return 0
                        else:  # if x[39] > 8.05
                          if x[35] <= 4.03:
                            return 2
                          else:  # if x[35] > 4.03
                            return 1
                    else:  # if x[35] > 5.31
                      if x[3] <= 12.51:
                        if x[39] <= 6.07:
                          if x[37] <= 0.79:
                            return 3
                          else:  # if x[37] > 0.79
                            if x[5] <= 3.62:
                              return 0
                            else:  # if x[5] > 3.62
                              return 1
                        else:  # if x[39] > 6.07
                          if x[5] <= 141.53:
                            return 1
                          else:  # if x[5] > 141.53
                            return 2
                      else:  # if x[3] > 12.51
                        if x[3] <= 108.12:
                          return 2
                        else:  # if x[3] > 108.12
                          return 1
                  else:  # if x[24] > 1.04
                    if x[35] <= -2.32:
                      if x[35] <= -29.55:
                        if x[33] <= -21.77:
                          return 1
                        else:  # if x[33] > -21.77
                          return 0
                      else:  # if x[35] > -29.55
                        if x[29] <= -1.55:
                          return 3
                        else:  # if x[29] > -1.55
                          return 1
                    else:  # if x[35] > -2.32
                      if x[28] <= -6.96:
                        return 1
                      else:  # if x[28] > -6.96
                        if x[33] <= 1.92:
                          return 0
                        else:  # if x[33] > 1.92
                          return 2
                else:  # if x[40] > -3.52
                  if x[3] <= 5.26:
                    if x[3] <= -4.04:
                      if x[5] <= 3.2:
                        if x[5] <= -9.59:
                          if x[27] <= 2.77:
                            if x[2] <= -1.34:
                              return 0
                            else:  # if x[2] > -1.34
                              return 3
                          else:  # if x[27] > 2.77
                            if x[38] <= -0.43:
                              return 2
                            else:  # if x[38] > -0.43
                              if x[27] <= 4.49:
                                return 0
                              else:  # if x[27] > 4.49
                                return 1
                        else:  # if x[5] > -9.59
                          if x[30] <= -1.28:
                            if x[8] <= -0.84:
                              return 3
                            else:  # if x[8] > -0.84
                              return 0
                          else:  # if x[30] > -1.28
                            if x[37] <= -2.55:
                              if x[19] <= -2.17:
                                return 3
                              else:  # if x[19] > -2.17
                                return 0
                            else:  # if x[37] > -2.55
                              if x[41] <= -4.36:
                                return 3
                              else:  # if x[41] > -4.36
                                if x[36] <= 1.04:
                                  if x[23] <= -1.83:
                                    if x[10] <= 1.23:
                                      return 3
                                    else:  # if x[10] > 1.23
                                      return 2
                                  else:  # if x[23] > -1.83
                                    if x[11] <= 3.85:
                                      if x[27] <= 358.21:
                                        if x[37] <= 2.81:
                                          if x[19] <= -2.26:
                                            return 0
                                          else:  # if x[19] > -2.26
                                            if x[41] <= 4.52:
                                              return 2
                                            else:  # if x[41] > 4.52
                                              if x[15] <= -1.3:
                                                return 2
                                              else:  # if x[15] > -1.3
                                                return 3
                                        else:  # if x[37] > 2.81
                                          return 0
                                      else:  # if x[27] > 358.21
                                        return 1
                                    else:  # if x[11] > 3.85
                                      if x[13] <= -0.48:
                                        return 3
                                      else:  # if x[13] > -0.48
                                        return 2
                                else:  # if x[36] > 1.04
                                  if x[29] <= 0.27:
                                    if x[9] <= -5.42:
                                      return 2
                                    else:  # if x[9] > -5.42
                                      if x[22] <= 1.18:
                                        return 3
                                      else:  # if x[22] > 1.18
                                        return 1
                                  else:  # if x[29] > 0.27
                                    return 0
                      else:  # if x[5] > 3.2
                        if x[5] <= 129.34:
                          if x[4] <= 1.94:
                            if x[10] <= 3.49:
                              if x[3] <= -216.91:
                                return 2
                              else:  # if x[3] > -216.91
                                if x[33] <= 182.76:
                                  if x[14] <= 2.15:
                                    if x[5] <= 3.93:
                                      if x[5] <= 3.78:
                                        return 0
                                      else:  # if x[5] > 3.78
                                        return 3
                                    else:  # if x[5] > 3.93
                                      if x[3] <= -4.24:
                                        return 0
                                      else:  # if x[3] > -4.24
                                        if x[20] <= -0.63:
                                          return 0
                                        else:  # if x[20] > -0.63
                                          return 3
                                  else:  # if x[14] > 2.15
                                    if x[2] <= 5.38:
                                      return 3
                                    else:  # if x[2] > 5.38
                                      return 0
                                else:  # if x[33] > 182.76
                                  return 2
                            else:  # if x[10] > 3.49
                              return 3
                          else:  # if x[4] > 1.94
                            if x[6] <= -0.36:
                              return 0
                            else:  # if x[6] > -0.36
                              if x[5] <= 5.56:
                                return 1
                              else:  # if x[5] > 5.56
                                return 3
                        else:  # if x[5] > 129.34
                          if x[16] <= 0.03:
                            if x[39] <= 225.12:
                              if x[7] <= 0.46:
                                return 1
                              else:  # if x[7] > 0.46
                                return 0
                            else:  # if x[39] > 225.12
                              return 3
                          else:  # if x[16] > 0.03
                            return 2
                    else:  # if x[3] > -4.04
                      if x[5] <= 2.57:
                        if x[5] <= -4.66:
                          if x[18] <= 0.49:
                            if x[3] <= 4.03:
                              if x[5] <= -355.71:
                                return 1
                              else:  # if x[5] > -355.71
                                if x[6] <= -2.92:
                                  return 0
                                else:  # if x[6] > -2.92
                                  if x[2] <= -0.86:
                                    if x[13] <= 0.0:
                                      return 3
                                    else:  # if x[13] > 0.0
                                      return 2
                                  else:  # if x[2] > -0.86
                                    if x[4] <= 8.51:
                                      if x[30] <= 2.67:
                                        if x[2] <= 2.85:
                                          return 3
                                        else:  # if x[2] > 2.85
                                          return 0
                                      else:  # if x[30] > 2.67
                                        return 0
                                    else:  # if x[4] > 8.51
                                      return 1
                            else:  # if x[3] > 4.03
                              if x[25] <= -0.17:
                                return 3
                              else:  # if x[25] > -0.17
                                return 0
                          else:  # if x[18] > 0.49
                            if x[36] <= -0.04:
                              if x[8] <= 0.91:
                                if x[33] <= 1.69:
                                  return 3
                                else:  # if x[33] > 1.69
                                  if x[32] <= -0.93:
                                    return 0
                                  else:  # if x[32] > -0.93
                                    return 1
                              else:  # if x[8] > 0.91
                                if x[6] <= 1.25:
                                  return 2
                                else:  # if x[6] > 1.25
                                  if x[35] <= 0.66:
                                    return 0
                                  else:  # if x[35] > 0.66
                                    return 1
                            else:  # if x[36] > -0.04
                              if x[4] <= -0.25:
                                if x[6] <= 0.43:
                                  return 0
                                else:  # if x[6] > 0.43
                                  return 3
                              else:  # if x[4] > -0.25
                                if x[40] <= -2.45:
                                  return 3
                                else:  # if x[40] > -2.45
                                  return 0
                        else:  # if x[5] > -4.66
                          if x[10] <= -3.58:
                            if x[7] <= 1.53:
                              if x[30] <= -2.91:
                                return 0
                              else:  # if x[30] > -2.91
                                if x[41] <= 1.69:
                                  return 1
                                else:  # if x[41] > 1.69
                                  return 0
                            else:  # if x[7] > 1.53
                              return 0
                          else:  # if x[10] > -3.58
                            if x[24] <= 0.7:
                              if x[16] <= 2.12:
                                if x[39] <= 3.53:
                                  if x[41] <= -1.85:
                                    if x[11] <= -1.11:
                                      if x[8] <= 1.78:
                                        if x[2] <= -1.58:
                                          return 0
                                        else:  # if x[2] > -1.58
                                          if x[16] <= -3.71:
                                            return 1
                                          else:  # if x[16] > -3.71
                                            if x[8] <= -1.04:
                                              if x[2] <= -0.57:
                                                return 0
                                              else:  # if x[2] > -0.57
                                                return 3
                                            else:  # if x[8] > -1.04
                                              return 3
                                      else:  # if x[8] > 1.78
                                        if x[2] <= 1.33:
                                          return 3
                                        else:  # if x[2] > 1.33
                                          return 0
                                    else:  # if x[11] > -1.11
                                      if x[39] <= -5.84:
                                        if x[36] <= -1.08:
                                          return 3
                                        else:  # if x[36] > -1.08
                                          return 2
                                      else:  # if x[39] > -5.84
                                        if x[22] <= 0.03:
                                          if x[39] <= -4.07:
                                            return 1
                                          else:  # if x[39] > -4.07
                                            return 0
                                        else:  # if x[22] > 0.03
                                          if x[19] <= -1.83:
                                            return 0
                                          else:  # if x[19] > -1.83
                                            if x[2] <= -0.16:
                                              if x[40] <= 1.52:
                                                if x[14] <= 0.13:
                                                  if x[37] <= -0.55:
                                                    return 2
                                                  else:  # if x[37] > -0.55
                                                    return 0
                                                else:  # if x[14] > 0.13
                                                  return 3
                                              else:  # if x[40] > 1.52
                                                return 1
                                            else:  # if x[2] > -0.16
                                              return 3
                                  else:  # if x[41] > -1.85
                                    if x[41] <= 3.2:
                                      if x[39] <= -4.21:
                                        if x[31] <= 2.33:
                                          return 2
                                        else:  # if x[31] > 2.33
                                          return 0
                                      else:  # if x[39] > -4.21
                                        if x[34] <= -1.62:
                                          if x[13] <= 0.66:
                                            if x[10] <= -1.38:
                                              if x[30] <= -0.71:
                                                return 0
                                              else:  # if x[30] > -0.71
                                                return 1
                                            else:  # if x[10] > -1.38
                                              if x[23] <= 0.66:
                                                if x[10] <= 1.8:
                                                  if x[28] <= 4.67:
                                                    return 3
                                                  else:  # if x[28] > 4.67
                                                    return 2
                                                else:  # if x[10] > 1.8
                                                  return 1
                                              else:  # if x[23] > 0.66
                                                if x[36] <= -1.05:
                                                  return 0
                                                else:  # if x[36] > -1.05
                                                  if x[24] <= -0.96:
                                                    return 0
                                                  else:  # if x[24] > -0.96
                                                    return 2
                                          else:  # if x[13] > 0.66
                                            if x[12] <= -0.57:
                                              return 2
                                            else:  # if x[12] > -0.57
                                              return 0
                                        else:  # if x[34] > -1.62
                                          if x[5] <= 1.01:
                                            if x[3] <= 4.19:
                                              if x[9] <= -2.89:
                                                if x[5] <= -0.09:
                                                  if x[35] <= -1.37:
                                                    return 3
                                                  else:  # if x[35] > -1.37
                                                    return 0
                                                else:  # if x[5] > -0.09
                                                  return 2
                                              else:  # if x[9] > -2.89
                                                if x[4] <= 5.34:
                                                  if x[4] <= 0.18:
                                                    if x[4] <= -3.79:
                                                      if x[9] <= -0.48:
                                                        return 0
                                                      else:  # if x[9] > -0.48
                                                        return 1
                                                    else:  # if x[4] > -3.79
                                                      if x[5] <= -4.57:
                                                        return 3
                                                      else:  # if x[5] > -4.57
                                                        if x[21] <= 4.22:
                                                          if x[16] <= -2.94:
                                                            if x[0] <= -0.05:
                                                              return 1
                                                            else:  # if x[0] > -0.05
                                                              return 0
                                                          else:  # if x[16] > -2.94
                                                            if x[41] <= -1.52:
                                                              if x[21] <= 0.06:
                                                                if x[31] <= 0.71:
                                                                  return 3
                                                                else:  # if x[31] > 0.71
                                                                  return 0
                                                              else:  # if x[21] > 0.06
                                                                return 0
                                                            else:  # if x[41] > -1.52
                                                              if x[35] <= -1.57:
                                                                if x[35] <= -1.63:
                                                                  return 0
                                                                else:  # if x[35] > -1.63
                                                                  return 2
                                                              else:  # if x[35] > -1.57
                                                                if x[16] <= -1.82:
                                                                  if x[4] <= -0.65:
                                                                    return 0
                                                                  else:  # if x[4] > -0.65
                                                                    return 3
                                                                else:  # if x[16] > -1.82
                                                                  return 0
                                                        else:  # if x[21] > 4.22
                                                          return 3
                                                  else:  # if x[4] > 0.18
                                                    if x[4] <= 0.24:
                                                      if x[13] <= -0.13:
                                                        if x[0] <= 0.21:
                                                          return 3
                                                        else:  # if x[0] > 0.21
                                                          return 0
                                                      else:  # if x[13] > -0.13
                                                        return 2
                                                    else:  # if x[4] > 0.24
                                                      if x[35] <= -1.91:
                                                        if x[13] <= -2.41:
                                                          return 0
                                                        else:  # if x[13] > -2.41
                                                          return 3
                                                      else:  # if x[35] > -1.91
                                                        if x[28] <= -1.43:
                                                          if x[41] <= -0.92:
                                                            return 0
                                                          else:  # if x[41] > -0.92
                                                            return 3
                                                        else:  # if x[28] > -1.43
                                                          if x[5] <= 0.77:
                                                            if x[26] <= -5.03:
                                                              return 3
                                                            else:  # if x[26] > -5.03
                                                              if x[39] <= -3.14:
                                                                if x[7] <= -0.61:
                                                                  return 0
                                                                else:  # if x[7] > -0.61
                                                                  return 2
                                                              else:  # if x[39] > -3.14
                                                                return 0
                                                          else:  # if x[5] > 0.77
                                                            if x[30] <= -1.3:
                                                              return 0
                                                            else:  # if x[30] > -1.3
                                                              return 3
                                                else:  # if x[4] > 5.34
                                                  if x[40] <= 2.02:
                                                    return 1
                                                  else:  # if x[40] > 2.02
                                                    return 3
                                            else:  # if x[3] > 4.19
                                              if x[6] <= -1.19:
                                                return 0
                                              else:  # if x[6] > -1.19
                                                return 2
                                          else:  # if x[5] > 1.01
                                            if x[39] <= -0.06:
                                              if x[9] <= 0.18:
                                                if x[12] <= -0.53:
                                                  if x[15] <= -3.87:
                                                    return 2
                                                  else:  # if x[15] > -3.87
                                                    return 0
                                                else:  # if x[12] > -0.53
                                                  if x[38] <= 1.39:
                                                    return 3
                                                  else:  # if x[38] > 1.39
                                                    return 0
                                              else:  # if x[9] > 0.18
                                                if x[4] <= -1.93:
                                                  return 1
                                                else:  # if x[4] > -1.93
                                                  if x[22] <= 0.88:
                                                    return 0
                                                  else:  # if x[22] > 0.88
                                                    if x[2] <= 0.11:
                                                      if x[41] <= -0.25:
                                                        return 1
                                                      else:  # if x[41] > -0.25
                                                        return 0
                                                    else:  # if x[2] > 0.11
                                                      return 3
                                            else:  # if x[39] > -0.06
                                              if x[4] <= -3.02:
                                                if x[39] <= 0.17:
                                                  return 0
                                                else:  # if x[39] > 0.17
                                                  return 1
                                              else:  # if x[4] > -3.02
                                                if x[41] <= 1.58:
                                                  return 0
                                                else:  # if x[41] > 1.58
                                                  if x[0] <= 0.61:
                                                    if x[37] <= -0.42:
                                                      return 2
                                                    else:  # if x[37] > -0.42
                                                      return 3
                                                  else:  # if x[0] > 0.61
                                                    return 0
                                    else:  # if x[41] > 3.2
                                      if x[37] <= -0.92:
                                        return 0
                                      else:  # if x[37] > -0.92
                                        if x[39] <= -2.6:
                                          if x[31] <= -0.12:
                                            if x[21] <= -2.29:
                                              return 0
                                            else:  # if x[21] > -2.29
                                              return 3
                                          else:  # if x[31] > -0.12
                                            if x[2] <= -0.69:
                                              return 2
                                            else:  # if x[2] > -0.69
                                              return 0
                                        else:  # if x[39] > -2.6
                                          if x[6] <= 1.78:
                                            return 3
                                          else:  # if x[6] > 1.78
                                            return 0
                                else:  # if x[39] > 3.53
                                  if x[21] <= 2.35:
                                    if x[35] <= -1.1:
                                      if x[8] <= 0.27:
                                        return 0
                                      else:  # if x[8] > 0.27
                                        if x[40] <= 0.58:
                                          return 2
                                        else:  # if x[40] > 0.58
                                          return 0
                                    else:  # if x[35] > -1.1
                                      if x[32] <= 0.13:
                                        if x[26] <= -0.51:
                                          if x[31] <= -0.59:
                                            return 3
                                          else:  # if x[31] > -0.59
                                            return 0
                                        else:  # if x[26] > -0.51
                                          return 2
                                      else:  # if x[32] > 0.13
                                        if x[12] <= -1.07:
                                          return 2
                                        else:  # if x[12] > -1.07
                                          return 3
                                  else:  # if x[21] > 2.35
                                    if x[1] <= -1.76:
                                      return 0
                                    else:  # if x[1] > -1.76
                                      if x[20] <= 5.9:
                                        return 2
                                      else:  # if x[20] > 5.9
                                        return 0
                              else:  # if x[16] > 2.12
                                if x[4] <= 1.26:
                                  if x[13] <= -0.58:
                                    if x[35] <= 5.84:
                                      return 0
                                    else:  # if x[35] > 5.84
                                      return 2
                                  else:  # if x[13] > -0.58
                                    if x[40] <= 1.93:
                                      if x[7] <= 0.23:
                                        if x[30] <= 0.89:
                                          return 3
                                        else:  # if x[30] > 0.89
                                          return 0
                                      else:  # if x[7] > 0.23
                                        return 0
                                    else:  # if x[40] > 1.93
                                      return 1
                                else:  # if x[4] > 1.26
                                  if x[1] <= -2.97:
                                    return 0
                                  else:  # if x[1] > -2.97
                                    if x[7] <= 1.37:
                                      if x[35] <= 4.47:
                                        return 1
                                      else:  # if x[35] > 4.47
                                        return 3
                                    else:  # if x[7] > 1.37
                                      return 3
                            else:  # if x[24] > 0.7
                              if x[11] <= -12.23:
                                return 3
                              else:  # if x[11] > -12.23
                                if x[18] <= -0.13:
                                  if x[41] <= -1.37:
                                    if x[39] <= 2.65:
                                      if x[27] <= 2.83:
                                        return 3
                                      else:  # if x[27] > 2.83
                                        return 0
                                    else:  # if x[39] > 2.65
                                      return 0
                                  else:  # if x[41] > -1.37
                                    if x[28] <= 3.29:
                                      if x[23] <= 3.06:
                                        if x[16] <= -3.58:
                                          return 1
                                        else:  # if x[16] > -3.58
                                          if x[21] <= 3.84:
                                            return 0
                                          else:  # if x[21] > 3.84
                                            if x[30] <= 0.25:
                                              return 3
                                            else:  # if x[30] > 0.25
                                              return 0
                                      else:  # if x[23] > 3.06
                                        return 3
                                    else:  # if x[28] > 3.29
                                      return 1
                                else:  # if x[18] > -0.13
                                  if x[30] <= -1.6:
                                    return 1
                                  else:  # if x[30] > -1.6
                                    if x[23] <= 4.37:
                                      if x[33] <= 208.69:
                                        if x[17] <= 13.97:
                                          if x[29] <= -1.53:
                                            if x[5] <= -3.8:
                                              return 3
                                            else:  # if x[5] > -3.8
                                              if x[21] <= 3.26:
                                                if x[40] <= 2.62:
                                                  return 0
                                                else:  # if x[40] > 2.62
                                                  return 3
                                              else:  # if x[21] > 3.26
                                                if x[14] <= 0.31:
                                                  return 2
                                                else:  # if x[14] > 0.31
                                                  return 0
                                          else:  # if x[29] > -1.53
                                            return 0
                                        else:  # if x[17] > 13.97
                                          return 3
                                      else:  # if x[33] > 208.69
                                        return 3
                                    else:  # if x[23] > 4.37
                                      if x[29] <= 5.0:
                                        return 0
                                      else:  # if x[29] > 5.0
                                        return 3
                      else:  # if x[5] > 2.57
                        if x[2] <= -0.75:
                          if x[5] <= 11.43:
                            if x[41] <= 3.39:
                              if x[4] <= 3.11:
                                return 0
                              else:  # if x[4] > 3.11
                                return 1
                            else:  # if x[41] > 3.39
                              if x[37] <= -0.74:
                                return 0
                              else:  # if x[37] > -0.74
                                return 3
                          else:  # if x[5] > 11.43
                            return 3
                        else:  # if x[2] > -0.75
                          if x[24] <= -1.84:
                            if x[36] <= -1.11:
                              return 0
                            else:  # if x[36] > -1.11
                              if x[4] <= 0.44:
                                return 3
                              else:  # if x[4] > 0.44
                                return 0
                          else:  # if x[24] > -1.84
                            if x[31] <= 1.82:
                              if x[26] <= 2.64:
                                if x[11] <= 1.86:
                                  if x[5] <= 4.75:
                                    if x[17] <= 1.34:
                                      if x[17] <= 0.96:
                                        if x[33] <= 2.57:
                                          return 0
                                        else:  # if x[33] > 2.57
                                          return 2
                                      else:  # if x[17] > 0.96
                                        return 3
                                    else:  # if x[17] > 1.34
                                      if x[20] <= -1.76:
                                        return 0
                                      else:  # if x[20] > -1.76
                                        return 1
                                  else:  # if x[5] > 4.75
                                    return 3
                                else:  # if x[11] > 1.86
                                  if x[26] <= -2.94:
                                    if x[9] <= -4.99:
                                      return 1
                                    else:  # if x[9] > -4.99
                                      return 0
                                  else:  # if x[26] > -2.94
                                    if x[41] <= 45.14:
                                      if x[7] <= -4.82:
                                        if x[41] <= 0.5:
                                          return 0
                                        else:  # if x[41] > 0.5
                                          return 1
                                      else:  # if x[7] > -4.82
                                        if x[0] <= 5.33:
                                          if x[3] <= -3.37:
                                            if x[17] <= 6.47:
                                              return 0
                                            else:  # if x[17] > 6.47
                                              return 3
                                          else:  # if x[3] > -3.37
                                            if x[16] <= -5.52:
                                              return 1
                                            else:  # if x[16] > -5.52
                                              if x[14] <= -3.14:
                                                return 0
                                              else:  # if x[14] > -3.14
                                                if x[39] <= 5.17:
                                                  if x[24] <= -1.72:
                                                    if x[34] <= 2.42:
                                                      return 0
                                                    else:  # if x[34] > 2.42
                                                      return 3
                                                  else:  # if x[24] > -1.72
                                                    return 3
                                                else:  # if x[39] > 5.17
                                                  if x[30] <= -0.38:
                                                    return 0
                                                  else:  # if x[30] > -0.38
                                                    return 3
                                        else:  # if x[0] > 5.33
                                          return 0
                                    else:  # if x[41] > 45.14
                                      return 1
                              else:  # if x[26] > 2.64
                                if x[34] <= 0.49:
                                  return 0
                                else:  # if x[34] > 0.49
                                  return 3
                            else:  # if x[31] > 1.82
                              if x[9] <= -1.99:
                                return 3
                              else:  # if x[9] > -1.99
                                return 0
                  else:  # if x[3] > 5.26
                    if x[5] <= -3.51:
                      if x[5] <= -284.76:
                        return 2
                      else:  # if x[5] > -284.76
                        if x[10] <= 0.64:
                          if x[28] <= 4.41:
                            if x[34] <= -3.2:
                              return 2
                            else:  # if x[34] > -3.2
                              if x[23] <= 4.43:
                                if x[29] <= 197.95:
                                  return 0
                                else:  # if x[29] > 197.95
                                  return 3
                              else:  # if x[23] > 4.43
                                return 3
                          else:  # if x[28] > 4.41
                            if x[14] <= 4.43:
                              return 3
                            else:  # if x[14] > 4.43
                              return 0
                        else:  # if x[10] > 0.64
                          if x[39] <= -2.78:
                            if x[11] <= -10.01:
                              return 0
                            else:  # if x[11] > -10.01
                              return 2
                          else:  # if x[39] > -2.78
                            if x[22] <= 2.93:
                              return 0
                            else:  # if x[22] > 2.93
                              return 1
                    else:  # if x[5] > -3.51
                      if x[1] <= -2.7:
                        if x[3] <= 9.26:
                          return 0
                        else:  # if x[3] > 9.26
                          return 2
                      else:  # if x[1] > -2.7
                        if x[3] <= 355.7:
                          if x[22] <= 3.44:
                            if x[23] <= 2.98:
                              if x[4] <= 9.66:
                                if x[11] <= 6.47:
                                  if x[26] <= -2.28:
                                    return 0
                                  else:  # if x[26] > -2.28
                                    if x[31] <= 6.82:
                                      if x[17] <= -6.69:
                                        return 0
                                      else:  # if x[17] > -6.69
                                        if x[10] <= -3.88:
                                          if x[0] <= -0.18:
                                            return 1
                                          else:  # if x[0] > -0.18
                                            return 2
                                        else:  # if x[10] > -3.88
                                          return 2
                                    else:  # if x[31] > 6.82
                                      return 0
                                else:  # if x[11] > 6.47
                                  if x[9] <= 5.91:
                                    return 3
                                  else:  # if x[9] > 5.91
                                    return 2
                              else:  # if x[4] > 9.66
                                return 1
                            else:  # if x[23] > 2.98
                              if x[7] <= -0.17:
                                return 2
                              else:  # if x[7] > -0.17
                                if x[4] <= 1.13:
                                  return 0
                                else:  # if x[4] > 1.13
                                  return 3
                          else:  # if x[22] > 3.44
                            if x[7] <= 0.44:
                              return 1
                            else:  # if x[7] > 0.44
                              return 2
                        else:  # if x[3] > 355.7
                          if x[22] <= -1.76:
                            return 1
                          else:  # if x[22] > -1.76
                            return 3
              else:  # if x[40] > 3.0
                if x[28] <= 2.13:
                  if x[4] <= -7.83:
                    if x[24] <= -0.9:
                      return 3
                    else:  # if x[24] > -0.9
                      return 1
                  else:  # if x[4] > -7.83
                    if x[9] <= 7.72:
                      if x[35] <= 5.12:
                        if x[5] <= 6.52:
                          if x[18] <= -0.96:
                            if x[21] <= -1.78:
                              return 3
                            else:  # if x[21] > -1.78
                              return 0
                          else:  # if x[18] > -0.96
                            if x[18] <= 0.78:
                              if x[27] <= 2.39:
                                if x[39] <= -5.99:
                                  return 2
                                else:  # if x[39] > -5.99
                                  if x[29] <= 1.18:
                                    if x[29] <= -1.95:
                                      return 3
                                    else:  # if x[29] > -1.95
                                      if x[30] <= 0.97:
                                        if x[19] <= -1.2:
                                          return 0
                                        else:  # if x[19] > -1.2
                                          return 1
                                      else:  # if x[30] > 0.97
                                        if x[21] <= 1.17:
                                          return 3
                                        else:  # if x[21] > 1.17
                                          return 2
                                  else:  # if x[29] > 1.18
                                    if x[41] <= 1.92:
                                      return 0
                                    else:  # if x[41] > 1.92
                                      return 3
                              else:  # if x[27] > 2.39
                                return 2
                            else:  # if x[18] > 0.78
                              return 0
                        else:  # if x[5] > 6.52
                          if x[10] <= -5.59:
                            return 1
                          else:  # if x[10] > -5.59
                            if x[18] <= -3.68:
                              return 0
                            else:  # if x[18] > -3.68
                              return 3
                      else:  # if x[35] > 5.12
                        if x[33] <= -3.69:
                          return 0
                        else:  # if x[33] > -3.69
                          return 3
                    else:  # if x[9] > 7.72
                      if x[22] <= -2.66:
                        if x[18] <= 0.72:
                          return 1
                        else:  # if x[18] > 0.72
                          return 0
                      else:  # if x[22] > -2.66
                        return 2
                else:  # if x[28] > 2.13
                  if x[13] <= -0.83:
                    if x[3] <= -2.29:
                      if x[35] <= 10.15:
                        return 1
                      else:  # if x[35] > 10.15
                        return 2
                    else:  # if x[3] > -2.29
                      if x[31] <= -4.25:
                        return 0
                      else:  # if x[31] > -4.25
                        if x[40] <= 6.25:
                          if x[20] <= 1.06:
                            if x[6] <= -2.17:
                              return 0
                            else:  # if x[6] > -2.17
                              return 3
                          else:  # if x[20] > 1.06
                            return 2
                        else:  # if x[40] > 6.25
                          if x[1] <= -1.03:
                            if x[3] <= 0.33:
                              return 3
                            else:  # if x[3] > 0.33
                              return 0
                          else:  # if x[1] > -1.03
                            return 1
                  else:  # if x[13] > -0.83
                    if x[18] <= 1.06:
                      if x[29] <= -5.03:
                        if x[19] <= 0.27:
                          if x[41] <= -9.47:
                            return 0
                          else:  # if x[41] > -9.47
                            return 1
                        else:  # if x[19] > 0.27
                          return 3
                      else:  # if x[29] > -5.03
                        if x[15] <= 6.41:
                          if x[24] <= -2.19:
                            return 0
                          else:  # if x[24] > -2.19
                            if x[41] <= 3.33:
                              if x[37] <= 1.74:
                                if x[27] <= 6.24:
                                  return 1
                                else:  # if x[27] > 6.24
                                  if x[35] <= 0.48:
                                    return 2
                                  else:  # if x[35] > 0.48
                                    return 1
                              else:  # if x[37] > 1.74
                                return 0
                            else:  # if x[41] > 3.33
                              if x[24] <= 1.04:
                                if x[28] <= 2.55:
                                  if x[12] <= 0.8:
                                    return 3
                                  else:  # if x[12] > 0.8
                                    return 1
                                else:  # if x[28] > 2.55
                                  if x[30] <= 0.62:
                                    return 1
                                  else:  # if x[30] > 0.62
                                    if x[8] <= -0.14:
                                      return 3
                                    else:  # if x[8] > -0.14
                                      return 1
                              else:  # if x[24] > 1.04
                                return 3
                        else:  # if x[15] > 6.41
                          if x[23] <= 0.37:
                            return 3
                          else:  # if x[23] > 0.37
                            return 2
                    else:  # if x[18] > 1.06
                      if x[13] <= -0.17:
                        if x[37] <= 0.1:
                          return 1
                        else:  # if x[37] > 0.1
                          return 3
                      else:  # if x[13] > -0.17
                        if x[24] <= 0.35:
                          return 1
                        else:  # if x[24] > 0.35
                          return 0
          else:  # if x[23] > 4.7
            if x[39] <= -7.24:
              if x[41] <= 4.18:
                if x[36] <= 0.91:
                  if x[27] <= 1.78:
                    if x[10] <= -2.81:
                      return 3
                    else:  # if x[10] > -2.81
                      return 2
                  else:  # if x[27] > 1.78
                    return 3
                else:  # if x[36] > 0.91
                  if x[38] <= 0.41:
                    return 1
                  else:  # if x[38] > 0.41
                    return 3
              else:  # if x[41] > 4.18
                if x[5] <= 108.68:
                  if x[21] <= 0.11:
                    return 0
                  else:  # if x[21] > 0.11
                    return 3
                else:  # if x[5] > 108.68
                  return 1
            else:  # if x[39] > -7.24
              if x[14] <= -2.55:
                if x[40] <= -0.78:
                  return 3
                else:  # if x[40] > -0.78
                  return 0
              else:  # if x[14] > -2.55
                if x[3] <= -7.05:
                  if x[9] <= -2.18:
                    if x[17] <= 3.39:
                      return 2
                    else:  # if x[17] > 3.39
                      return 0
                  else:  # if x[9] > -2.18
                    if x[27] <= 8.2:
                      return 3
                    else:  # if x[27] > 8.2
                      if x[41] <= 2.49:
                        return 1
                      else:  # if x[41] > 2.49
                        return 2
                else:  # if x[3] > -7.05
                  if x[33] <= -7.94:
                    if x[22] <= -1.01:
                      if x[20] <= 0.02:
                        return 3
                      else:  # if x[20] > 0.02
                        return 2
                    else:  # if x[22] > -1.01
                      return 0
                  else:  # if x[33] > -7.94
                    if x[0] <= 6.32:
                      if x[9] <= 6.53:
                        if x[23] <= 356.9:
                          if x[25] <= 5.65:
                            if x[8] <= -2.94:
                              if x[4] <= -1.64:
                                return 2
                              else:  # if x[4] > -1.64
                                if x[28] <= 0.14:
                                  return 3
                                else:  # if x[28] > 0.14
                                  return 0
                            else:  # if x[8] > -2.94
                              if x[21] <= -4.51:
                                if x[17] <= 10.43:
                                  if x[24] <= 0.58:
                                    return 1
                                  else:  # if x[24] > 0.58
                                    return 0
                                else:  # if x[17] > 10.43
                                  return 3
                              else:  # if x[21] > -4.51
                                if x[10] <= -12.03:
                                  return 1
                                else:  # if x[10] > -12.03
                                  if x[37] <= 5.81:
                                    if x[0] <= -8.36:
                                      return 0
                                    else:  # if x[0] > -8.36
                                      if x[20] <= 6.45:
                                        if x[26] <= -2.67:
                                          if x[8] <= 0.55:
                                            return 3
                                          else:  # if x[8] > 0.55
                                            return 2
                                        else:  # if x[26] > -2.67
                                          if x[32] <= -2.63:
                                            if x[38] <= -0.48:
                                              return 2
                                            else:  # if x[38] > -0.48
                                              return 3
                                          else:  # if x[32] > -2.63
                                            if x[1] <= -6.34:
                                              if x[13] <= -5.18:
                                                return 3
                                              else:  # if x[13] > -5.18
                                                return 0
                                            else:  # if x[1] > -6.34
                                              if x[8] <= 3.5:
                                                if x[21] <= 4.48:
                                                  if x[9] <= -7.05:
                                                    if x[16] <= -2.44:
                                                      return 0
                                                    else:  # if x[16] > -2.44
                                                      return 3
                                                  else:  # if x[9] > -7.05
                                                    if x[21] <= -4.3:
                                                      if x[21] <= -4.35:
                                                        return 3
                                                      else:  # if x[21] > -4.35
                                                        return 0
                                                    else:  # if x[21] > -4.3
                                                      if x[31] <= 2.74:
                                                        if x[26] <= 2.67:
                                                          if x[21] <= -3.92:
                                                            if x[21] <= -3.95:
                                                              return 3
                                                            else:  # if x[21] > -3.95
                                                              return 0
                                                          else:  # if x[21] > -3.92
                                                            return 3
                                                        else:  # if x[26] > 2.67
                                                          if x[20] <= 2.2:
                                                            return 3
                                                          else:  # if x[20] > 2.2
                                                            return 0
                                                      else:  # if x[31] > 2.74
                                                        if x[9] <= 4.4:
                                                          return 3
                                                        else:  # if x[9] > 4.4
                                                          return 0
                                                else:  # if x[21] > 4.48
                                                  if x[22] <= -2.53:
                                                    return 1
                                                  else:  # if x[22] > -2.53
                                                    return 3
                                              else:  # if x[8] > 3.5
                                                if x[30] <= 2.06:
                                                  return 3
                                                else:  # if x[30] > 2.06
                                                  return 0
                                      else:  # if x[20] > 6.45
                                        return 0
                                  else:  # if x[37] > 5.81
                                    return 0
                          else:  # if x[25] > 5.65
                            return 0
                        else:  # if x[23] > 356.9
                          if x[40] <= -0.4:
                            return 3
                          else:  # if x[40] > -0.4
                            return 1
                      else:  # if x[9] > 6.53
                        if x[8] <= 0.59:
                          if x[20] <= -0.59:
                            return 0
                          else:  # if x[20] > -0.59
                            return 3
                        else:  # if x[8] > 0.59
                          if x[14] <= 4.59:
                            return 2
                          else:  # if x[14] > 4.59
                            return 0
                    else:  # if x[0] > 6.32
                      if x[32] <= 2.06:
                        return 0
                      else:  # if x[32] > 2.06
                        return 3
      else:  # if x[21] > 4.64
        if x[23] <= -4.19:
          if x[23] <= -250.86:
            if x[21] <= 193.57:
              if x[22] <= -3.45:
                if x[4] <= -2.47:
                  return 1
                else:  # if x[4] > -2.47
                  return 2
              else:  # if x[22] > -3.45
                if x[21] <= 5.23:
                  return 3
                else:  # if x[21] > 5.23
                  return 2
            else:  # if x[21] > 193.57
              if x[27] <= -6.95:
                return 0
              else:  # if x[27] > -6.95
                return 3
          else:  # if x[23] > -250.86
            if x[40] <= -3.94:
              if x[14] <= -1.06:
                return 0
              else:  # if x[14] > -1.06
                if x[25] <= -1.1:
                  if x[38] <= 0.69:
                    if x[33] <= 2.61:
                      return 0
                    else:  # if x[33] > 2.61
                      return 3
                  else:  # if x[38] > 0.69
                    return 2
                else:  # if x[25] > -1.1
                  if x[24] <= -2.14:
                    if x[10] <= -2.47:
                      return 3
                    else:  # if x[10] > -2.47
                      return 0
                  else:  # if x[24] > -2.14
                    if x[34] <= -0.79:
                      if x[18] <= 2.43:
                        if x[31] <= -1.33:
                          return 0
                        else:  # if x[31] > -1.33
                          return 1
                      else:  # if x[18] > 2.43
                        if x[1] <= -1.92:
                          return 3
                        else:  # if x[1] > -1.92
                          return 0
                    else:  # if x[34] > -0.79
                      return 2
            else:  # if x[40] > -3.94
              if x[13] <= 0.39:
                if x[8] <= -0.73:
                  if x[21] <= 294.58:
                    if x[28] <= 7.69:
                      if x[7] <= 2.84:
                        if x[23] <= -7.04:
                          if x[1] <= 2.89:
                            return 0
                          else:  # if x[1] > 2.89
                            if x[14] <= -1.06:
                              return 0
                            else:  # if x[14] > -1.06
                              return 3
                        else:  # if x[23] > -7.04
                          if x[21] <= 10.04:
                            return 0
                          else:  # if x[21] > 10.04
                            return 2
                      else:  # if x[7] > 2.84
                        return 3
                    else:  # if x[28] > 7.69
                      return 1
                  else:  # if x[21] > 294.58
                    return 3
                else:  # if x[8] > -0.73
                  if x[21] <= 7.18:
                    if x[23] <= -8.21:
                      if x[31] <= -1.72:
                        return 0
                      else:  # if x[31] > -1.72
                        if x[24] <= -2.06:
                          if x[35] <= 7.63:
                            return 0
                          else:  # if x[35] > 7.63
                            return 2
                        else:  # if x[24] > -2.06
                          return 3
                    else:  # if x[23] > -8.21
                      if x[34] <= -1.58:
                        if x[9] <= 4.64:
                          return 3
                        else:  # if x[9] > 4.64
                          if x[39] <= 6.71:
                            if x[20] <= 0.23:
                              return 1
                            else:  # if x[20] > 0.23
                              return 0
                          else:  # if x[39] > 6.71
                            return 2
                      else:  # if x[34] > -1.58
                        if x[28] <= 3.75:
                          if x[21] <= 6.66:
                            if x[22] <= 1.92:
                              return 0
                            else:  # if x[22] > 1.92
                              if x[33] <= 0.01:
                                return 3
                              else:  # if x[33] > 0.01
                                return 0
                          else:  # if x[21] > 6.66
                            if x[25] <= -0.37:
                              return 2
                            else:  # if x[25] > -0.37
                              return 0
                        else:  # if x[28] > 3.75
                          return 1
                  else:  # if x[21] > 7.18
                    if x[23] <= -8.47:
                      if x[40] <= 5.15:
                        if x[21] <= 191.2:
                          if x[10] <= 3.76:
                            if x[2] <= 0.94:
                              if x[40] <= -2.58:
                                if x[1] <= 0.03:
                                  return 0
                                else:  # if x[1] > 0.03
                                  if x[30] <= -0.85:
                                    return 3
                                  else:  # if x[30] > -0.85
                                    return 1
                              else:  # if x[40] > -2.58
                                if x[17] <= 119.08:
                                  return 0
                                else:  # if x[17] > 119.08
                                  return 2
                            else:  # if x[2] > 0.94
                              if x[16] <= 0.59:
                                if x[1] <= -1.03:
                                  if x[15] <= 4.95:
                                    return 3
                                  else:  # if x[15] > 4.95
                                    return 0
                                else:  # if x[1] > -1.03
                                  return 2
                              else:  # if x[16] > 0.59
                                return 0
                          else:  # if x[10] > 3.76
                            if x[4] <= 2.64:
                              return 0
                            else:  # if x[4] > 2.64
                              return 1
                        else:  # if x[21] > 191.2
                          if x[13] <= -0.51:
                            return 2
                          else:  # if x[13] > -0.51
                            return 3
                      else:  # if x[40] > 5.15
                        return 1
                    else:  # if x[23] > -8.47
                      if x[0] <= -1.12:
                        if x[21] <= 184.32:
                          return 0
                        else:  # if x[21] > 184.32
                          return 3
                      else:  # if x[0] > -1.12
                        if x[0] <= 0.46:
                          if x[29] <= 7.13:
                            return 2
                          else:  # if x[29] > 7.13
                            return 0
                        else:  # if x[0] > 0.46
                          if x[2] <= 0.62:
                            return 0
                          else:  # if x[2] > 0.62
                            return 3
              else:  # if x[13] > 0.39
                if x[25] <= -2.21:
                  if x[21] <= 12.4:
                    return 0
                  else:  # if x[21] > 12.4
                    return 2
                else:  # if x[25] > -2.21
                  if x[4] <= 6.94:
                    if x[28] <= -6.37:
                      return 3
                    else:  # if x[28] > -6.37
                      if x[16] <= 3.71:
                        if x[21] <= 291.42:
                          if x[28] <= -2.9:
                            if x[21] <= 8.34:
                              return 3
                            else:  # if x[21] > 8.34
                              return 0
                          else:  # if x[28] > -2.9
                            if x[21] <= 5.57:
                              if x[21] <= 5.57:
                                return 0
                              else:  # if x[21] > 5.57
                                return 3
                            else:  # if x[21] > 5.57
                              return 0
                        else:  # if x[21] > 291.42
                          return 2
                      else:  # if x[16] > 3.71
                        if x[38] <= 0.38:
                          return 0
                        else:  # if x[38] > 0.38
                          if x[17] <= -8.16:
                            return 1
                          else:  # if x[17] > -8.16
                            return 2
                  else:  # if x[4] > 6.94
                    return 1
        else:  # if x[23] > -4.19
          if x[23] <= 9.26:
            if x[21] <= 356.8:
              if x[1] <= 2.61:
                if x[19] <= -4.76:
                  return 0
                else:  # if x[19] > -4.76
                  if x[24] <= -1.72:
                    if x[18] <= -0.95:
                      return 0
                    else:  # if x[18] > -0.95
                      if x[15] <= 2.17:
                        if x[36] <= -1.74:
                          return 0
                        else:  # if x[36] > -1.74
                          return 1
                      else:  # if x[15] > 2.17
                        return 2
                  else:  # if x[24] > -1.72
                    if x[23] <= 4.17:
                      if x[2] <= -5.9:
                        return 0
                      else:  # if x[2] > -5.9
                        if x[40] <= 10.25:
                          if x[31] <= -5.18:
                            return 3
                          else:  # if x[31] > -5.18
                            if x[30] <= 2.13:
                              if x[8] <= 9.08:
                                if x[21] <= 5.25:
                                  if x[39] <= 1.87:
                                    if x[9] <= 4.48:
                                      if x[34] <= -0.81:
                                        return 3
                                      else:  # if x[34] > -0.81
                                        if x[28] <= 1.34:
                                          return 0
                                        else:  # if x[28] > 1.34
                                          return 1
                                    else:  # if x[9] > 4.48
                                      if x[40] <= 1.8:
                                        return 2
                                      else:  # if x[40] > 1.8
                                        return 0
                                  else:  # if x[39] > 1.87
                                    if x[25] <= -2.16:
                                      return 0
                                    else:  # if x[25] > -2.16
                                      return 2
                                else:  # if x[21] > 5.25
                                  if x[35] <= -10.72:
                                    if x[29] <= -14.08:
                                      return 3
                                    else:  # if x[29] > -14.08
                                      if x[21] <= 6.27:
                                        return 3
                                      else:  # if x[21] > 6.27
                                        return 2
                                  else:  # if x[35] > -10.72
                                    if x[19] <= 3.66:
                                      if x[0] <= -3.05:
                                        if x[23] <= 1.22:
                                          return 0
                                        else:  # if x[23] > 1.22
                                          return 2
                                      else:  # if x[0] > -3.05
                                        if x[19] <= -2.81:
                                          if x[36] <= 0.7:
                                            return 2
                                          else:  # if x[36] > 0.7
                                            return 0
                                        else:  # if x[19] > -2.81
                                          if x[6] <= -2.35:
                                            if x[29] <= 0.99:
                                              return 2
                                            else:  # if x[29] > 0.99
                                              return 0
                                          else:  # if x[6] > -2.35
                                            if x[35] <= 21.18:
                                              if x[10] <= -6.57:
                                                if x[16] <= -3.79:
                                                  return 1
                                                else:  # if x[16] > -3.79
                                                  return 2
                                              else:  # if x[10] > -6.57
                                                return 2
                                            else:  # if x[35] > 21.18
                                              if x[29] <= 1.58:
                                                return 2
                                              else:  # if x[29] > 1.58
                                                return 3
                                    else:  # if x[19] > 3.66
                                      if x[23] <= -2.23:
                                        return 0
                                      else:  # if x[23] > -2.23
                                        return 2
                              else:  # if x[8] > 9.08
                                return 0
                            else:  # if x[30] > 2.13
                              if x[9] <= 6.26:
                                return 0
                              else:  # if x[9] > 6.26
                                return 2
                        else:  # if x[40] > 10.25
                          return 1
                    else:  # if x[23] > 4.17
                      if x[21] <= 7.51:
                        if x[22] <= 3.1:
                          if x[41] <= 15.74:
                            if x[30] <= -0.59:
                              if x[9] <= -26.55:
                                return 2
                              else:  # if x[9] > -26.55
                                return 3
                            else:  # if x[30] > -0.59
                              if x[20] <= -5.05:
                                return 0
                              else:  # if x[20] > -5.05
                                return 2
                          else:  # if x[41] > 15.74
                            if x[15] <= 2.37:
                              return 3
                            else:  # if x[15] > 2.37
                              return 1
                        else:  # if x[22] > 3.1
                          return 1
                      else:  # if x[21] > 7.51
                        if x[29] <= 22.07:
                          if x[20] <= -1.48:
                            if x[13] <= -0.37:
                              if x[36] <= 0.38:
                                return 2
                              else:  # if x[36] > 0.38
                                return 0
                            else:  # if x[13] > -0.37
                              return 3
                          else:  # if x[20] > -1.48
                            if x[21] <= 354.31:
                              return 2
                            else:  # if x[21] > 354.31
                              if x[8] <= 0.49:
                                return 0
                              else:  # if x[8] > 0.49
                                return 3
                        else:  # if x[29] > 22.07
                          return 3
              else:  # if x[1] > 2.61
                if x[14] <= 0.51:
                  return 0
                else:  # if x[14] > 0.51
                  return 2
            else:  # if x[21] > 356.8
              if x[16] <= -2.0:
                return 1
              else:  # if x[16] > -2.0
                return 3
          else:  # if x[23] > 9.26
            if x[21] <= 7.11:
              if x[12] <= 0.91:
                if x[16] <= 2.22:
                  return 3
                else:  # if x[16] > 2.22
                  if x[1] <= -0.8:
                    return 3
                  else:  # if x[1] > -0.8
                    return 2
              else:  # if x[12] > 0.91
                if x[28] <= -1.92:
                  return 2
                else:  # if x[28] > -1.92
                  if x[36] <= 5.66:
                    return 0
                  else:  # if x[36] > 5.66
                    return 3
            else:  # if x[21] > 7.11
              if x[40] <= 5.03:
                if x[21] <= 128.19:
                  if x[0] <= 1.78:
                    if x[4] <= -6.66:
                      return 1
                    else:  # if x[4] > -6.66
                      if x[4] <= -0.26:
                        if x[28] <= -0.09:
                          if x[26] <= 0.4:
                            if x[30] <= 0.14:
                              return 3
                            else:  # if x[30] > 0.14
                              if x[27] <= 37.64:
                                return 1
                              else:  # if x[27] > 37.64
                                return 2
                          else:  # if x[26] > 0.4
                            if x[4] <= -3.59:
                              return 1
                            else:  # if x[4] > -3.59
                              return 2
                        else:  # if x[28] > -0.09
                          if x[30] <= 1.04:
                            if x[40] <= 4.85:
                              if x[34] <= -0.87:
                                return 0
                              else:  # if x[34] > -0.87
                                if x[39] <= -11.8:
                                  if x[15] <= 24.79:
                                    return 3
                                  else:  # if x[15] > 24.79
                                    return 2
                                else:  # if x[39] > -11.8
                                  return 2
                            else:  # if x[40] > 4.85
                              return 1
                          else:  # if x[30] > 1.04
                            return 3
                      else:  # if x[4] > -0.26
                        if x[4] <= 4.46:
                          if x[21] <= 8.16:
                            if x[28] <= 1.79:
                              return 2
                            else:  # if x[28] > 1.79
                              return 3
                          else:  # if x[21] > 8.16
                            return 2
                        else:  # if x[4] > 4.46
                          return 1
                  else:  # if x[0] > 1.78
                    if x[35] <= 7.08:
                      return 0
                    else:  # if x[35] > 7.08
                      return 3
                else:  # if x[21] > 128.19
                  if x[21] <= 349.98:
                    if x[40] <= -2.6:
                      return 1
                    else:  # if x[40] > -2.6
                      if x[23] <= 235.86:
                        return 0
                      else:  # if x[23] > 235.86
                        return 2
                  else:  # if x[21] > 349.98
                    return 3
              else:  # if x[40] > 5.03
                if x[9] <= 1.82:
                  if x[28] <= 1.47:
                    return 2
                  else:  # if x[28] > 1.47
                    if x[14] <= 0.53:
                      return 1
                    else:  # if x[14] > 0.53
                      return 3
                else:  # if x[9] > 1.82
                  return 1
  else:  # if x[22] > 4.76
    if x[10] <= 3.09:
      if x[34] <= 4.69:
        if x[21] <= 6.38:
          if x[21] <= -7.62:
            if x[0] <= -0.95:
              if x[40] <= -2.22:
                if x[19] <= -2.61:
                  return 0
                else:  # if x[19] > -2.61
                  return 1
              else:  # if x[40] > -2.22
                return 2
            else:  # if x[0] > -0.95
              if x[29] <= -8.48:
                if x[1] <= -0.2:
                  if x[9] <= -10.23:
                    return 2
                  else:  # if x[9] > -10.23
                    return 3
                else:  # if x[1] > -0.2
                  return 1
              else:  # if x[29] > -8.48
                if x[6] <= 2.07:
                  if x[26] <= -3.52:
                    return 0
                  else:  # if x[26] > -3.52
                    if x[17] <= -101.04:
                      return 1
                    else:  # if x[17] > -101.04
                      return 2
                else:  # if x[6] > 2.07
                  return 0
          else:  # if x[21] > -7.62
            if x[4] <= -10.91:
              return 1
            else:  # if x[4] > -10.91
              if x[19] <= -3.4:
                if x[11] <= 4.6:
                  return 0
                else:  # if x[11] > 4.6
                  return 3
              else:  # if x[19] > -3.4
                if x[39] <= -5.31:
                  if x[41] <= 7.12:
                    if x[7] <= 1.01:
                      return 2
                    else:  # if x[7] > 1.01
                      return 3
                  else:  # if x[41] > 7.12
                    return 3
                else:  # if x[39] > -5.31
                  if x[27] <= 7.4:
                    if x[15] <= -7.97:
                      if x[32] <= -0.47:
                        return 0
                      else:  # if x[32] > -0.47
                        return 1
                    else:  # if x[15] > -7.97
                      if x[40] <= 2.57:
                        if x[22] <= 4.79:
                          return 1
                        else:  # if x[22] > 4.79
                          if x[12] <= 7.67:
                            if x[35] <= 29.46:
                              return 3
                            else:  # if x[35] > 29.46
                              if x[33] <= -33.16:
                                return 0
                              else:  # if x[33] > -33.16
                                return 1
                          else:  # if x[12] > 7.67
                            return 0
                      else:  # if x[40] > 2.57
                        if x[28] <= 4.42:
                          return 3
                        else:  # if x[28] > 4.42
                          if x[11] <= -4.65:
                            return 3
                          else:  # if x[11] > -4.65
                            return 1
                  else:  # if x[27] > 7.4
                    if x[40] <= -6.93:
                      return 1
                    else:  # if x[40] > -6.93
                      if x[7] <= -0.98:
                        return 2
                      else:  # if x[7] > -0.98
                        return 0
        else:  # if x[21] > 6.38
          if x[34] <= -6.89:
            return 1
          else:  # if x[34] > -6.89
            if x[28] <= 7.22:
              if x[6] <= 1.05:
                if x[40] <= 4.67:
                  if x[28] <= -2.2:
                    return 3
                  else:  # if x[28] > -2.2
                    if x[0] <= -2.44:
                      return 0
                    else:  # if x[0] > -2.44
                      if x[39] <= 34.75:
                        return 2
                      else:  # if x[39] > 34.75
                        return 1
                else:  # if x[40] > 4.67
                  return 1
              else:  # if x[6] > 1.05
                if x[8] <= -0.81:
                  return 0
                else:  # if x[8] > -0.81
                  return 1
            else:  # if x[28] > 7.22
              return 1
      else:  # if x[34] > 4.69
        if x[25] <= -1.13:
          if x[4] <= -2.5:
            if x[20] <= -0.71:
              return 0
            else:  # if x[20] > -0.71
              return 1
          else:  # if x[4] > -2.5
            if x[33] <= 0.43:
              return 3
            else:  # if x[33] > 0.43
              if x[36] <= -0.08:
                return 0
              else:  # if x[36] > -0.08
                return 2
        else:  # if x[25] > -1.13
          if x[35] <= -6.56:
            if x[17] <= -3.3:
              if x[10] <= -4.08:
                if x[18] <= -0.17:
                  return 1
                else:  # if x[18] > -0.17
                  return 2
              else:  # if x[10] > -4.08
                return 3
            else:  # if x[17] > -3.3
              return 1
          else:  # if x[35] > -6.56
            if x[31] <= -1.76:
              return 3
            else:  # if x[31] > -1.76
              if x[19] <= 1.49:
                if x[32] <= -2.36:
                  return 2
                else:  # if x[32] > -2.36
                  if x[31] <= 2.24:
                    return 1
                  else:  # if x[31] > 2.24
                    return 2
              else:  # if x[19] > 1.49
                if x[5] <= -3.54:
                  return 2
                else:  # if x[5] > -3.54
                  return 0
    else:  # if x[10] > 3.09
      if x[17] <= -8.58:
        if x[23] <= -7.85:
          if x[11] <= -6.33:
            if x[5] <= -26.97:
              return 1
            else:  # if x[5] > -26.97
              return 3
          else:  # if x[11] > -6.33
            return 1
        else:  # if x[23] > -7.85
          if x[24] <= 1.88:
            return 1
          else:  # if x[24] > 1.88
            return 0
      else:  # if x[17] > -8.58
        if x[13] <= -1.28:
          if x[34] <= 2.77:
            if x[34] <= 2.14:
              if x[10] <= 8.15:
                if x[9] <= -7.11:
                  return 2
                else:  # if x[9] > -7.11
                  return 3
              else:  # if x[10] > 8.15
                return 1
            else:  # if x[34] > 2.14
              if x[21] <= -7.53:
                return 2
              else:  # if x[21] > -7.53
                return 0
          else:  # if x[34] > 2.77
            if x[23] <= -5.83:
              if x[8] <= 0.66:
                return 3
              else:  # if x[8] > 0.66
                return 0
            else:  # if x[23] > -5.83
              if x[1] <= -5.64:
                return 0
              else:  # if x[1] > -5.64
                if x[16] <= 3.13:
                  return 2
                else:  # if x[16] > 3.13
                  return 1
        else:  # if x[13] > -1.28
          if x[16] <= 4.82:
            if x[5] <= 8.79:
              if x[9] <= -9.91:
                if x[16] <= 3.66:
                  return 1
                else:  # if x[16] > 3.66
                  return 2
              else:  # if x[9] > -9.91
                if x[17] <= -5.98:
                  return 3
                else:  # if x[17] > -5.98
                  if x[19] <= 1.24:
                    if x[15] <= 4.34:
                      if x[34] <= -6.47:
                        return 2
                      else:  # if x[34] > -6.47
                        return 1
                    else:  # if x[15] > 4.34
                      if x[23] <= -4.55:
                        return 1
                      else:  # if x[23] > -4.55
                        return 2
                  else:  # if x[19] > 1.24
                    if x[29] <= 4.11:
                      return 3
                    else:  # if x[29] > 4.11
                      return 2
            else:  # if x[5] > 8.79
              return 3
          else:  # if x[16] > 4.82
            if x[19] <= -2.62:
              if x[41] <= -2.21:
                return 3
              else:  # if x[41] > -2.21
                return 1
            else:  # if x[19] > -2.62
              if x[7] <= -3.03:
                return 3
              else:  # if x[7] > -3.03
                if x[8] <= 3.95:
                  if x[31] <= -1.59:
                    if x[26] <= 0.86:
                      return 1
                    else:  # if x[26] > 0.86
                      if x[3] <= -19.74:
                        return 2
                      else:  # if x[3] > -19.74
                        return 3
                  else:  # if x[31] > -1.59
                    if x[17] <= -7.91:
                      if x[17] <= -7.99:
                        return 1
                      else:  # if x[17] > -7.99
                        return 3
                    else:  # if x[17] > -7.91
                      if x[17] <= 10.56:
                        return 1
                      else:  # if x[17] > 10.56
                        if x[17] <= 11.69:
                          return 3
                        else:  # if x[17] > 11.69
                          if x[0] <= -1.73:
                            return 3
                          else:  # if x[0] > -1.73
                            return 1
                else:  # if x[8] > 3.95
                  if x[35] <= -3.67:
                    return 3
                  else:  # if x[35] > -3.67
                    return 1