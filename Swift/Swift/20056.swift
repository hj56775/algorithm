//
//  20056.swift
//  Swift
//
//  Created by 유한준 on 2021/10/03.
//

import Foundation

func Q20056() {
    let mNK = readLine()!.split(separator: " ").map{ Int($0)! }
    let n = mNK[0]
    let m = mNK[1]
    let k = mNK[2]
    var fireballs = [fireball]()
    let row = [fireball?](repeating: nil, count: n)
    var map = [[fireball?]](repeating: row, count: n)

    let dir = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]

    for _ in 0..<m {
        let fireballInfo = readLine()!.split(separator: " ").map{ Int($0)! }
        let tempFireball = fireball(r: fireballInfo[0] - 1, c: fireballInfo[1] - 1, m: fireballInfo[2], s: fireballInfo[3], d: fireballInfo[4])
        fireballs.append(tempFireball)
        //map[tempFireball.r][tempFireball.c] = tempFireball
    }

    var twoAndMore =  [[Int]: [fireball]]()

    for _ in 0..<k {
        for var fireball in fireballs {
            let nextRow = fireball.r + dir[fireball.d].1 * fireball.s
            let nextCol = fireball.c + dir[fireball.d].0 * fireball.s
            if map[nextRow][nextCol] == nil {
                fireball.r += dir[fireball.d].1 * fireball.s
                fireball.c += dir[fireball.d].0 * fireball.s
                map[fireball.r][fireball.c] = fireball
            }
            else {
                if twoAndMore[[nextRow, nextCol]] != nil {
                    twoAndMore[[nextRow, nextCol]]!.append(fireball)
                }
                else {
                    twoAndMore[[nextRow, nextCol]] = [fireball]
                }
            }
        }
        map = [[fireball?]](repeating: row, count: n)
    }


    struct fireball {
        var r: Int
        var c: Int
        let m: Int
        let s: Int
        let d: Int
    }

}

