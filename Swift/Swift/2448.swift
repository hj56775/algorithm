//
//  2448.swift
//  PSSwift
//
//  Created by 유한준 on 2021/10/10.
//

//다시 풀어보기
import Foundation

func Q2448() {
    
    var array = [
      "  *   ",
      " * *  ",
      "***** "]
    
    let n = Int(readLine()!)!
    
    var num = 3
    while num < n {
      let count = array.count

      var temp: [String] = []

      for a in array {
        temp.append(a + a)
      }

      for i in 0 ..< count {
        var str = array[i]
        str = String(repeating: " ", count: count) + str + String(repeating: " ", count: count)
        array[i] = str
      }

      array.append(contentsOf: temp)
      num *= 2
    }

    for s in array {
      print(s)
    }
}
