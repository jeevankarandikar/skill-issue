export type AgentRow = {
  label: string
  calls: number
  lastAt: number
  isDone: boolean
}

export type Limit = { kind: string; percentUsed: number; resetsAt?: string }

export type Gauge = { tokens?: number; window: number; limits: Limit[] }

declare module 'claude-code' {
  interface PluginState {
    'fleet-gauge': { agents: Record<string, AgentRow>; gauge: Gauge | null }
  }
}
