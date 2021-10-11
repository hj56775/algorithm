//
//  1018.swift
//  PSSwift
//
//  Created by 유한준 on 2021/10/11.
//

import Foundation

func Q1018() {
    let mAndN = readLine()!.split(separator: " ").map { Int($0)! }
    let m = mAndN[0]
    let n = mAndN[1]
    var map = [[String]]()

    for _ in 0..<m {
        map.append(readLine()!.map{ String($0)})
    }
    
    var minimumValue: Int = 64
    
    for i in 0..<m - 7 {
        for j in 0..<n - 7 {
            if map[i][j] == "W" {
                var count: Int = 0
                for y in i..<i + 8 {
                    for x in j..<j + 8 {
                        if ((x + y) % 2 == 0 && map[y][x] != "W") || ((x + y) % 2 == 1 && map[y][x] != "B") {
                            count += 1
                        }
                    }
                }
                count = min(count, 64 - count)
                minimumValue = min(minimumValue, count)
            }
            else {
                var count: Int = 0
                for y in i..<i + 8 {
                    for x in j..<j + 8 {
                        if ((x + y) % 2 == 0 && map[y][x] != "B") || ((x + y) % 2 == 1 && map[y][x] != "W") {
                            count += 1
                        }
                    }
                }
                count = min(count, 64 - count)
                minimumValue = min(minimumValue, count)
            }
        }
    }
    print(minimumValue)
}
