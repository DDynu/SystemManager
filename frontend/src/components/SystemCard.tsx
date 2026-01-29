import { SystemStatus } from "../enums/SystemStatus"

export default function SystemCard({systemName, systemStatus}: {systemName: string, systemStatus: string}) {
  return (
    <article>
      <h2>
        System Name: {systemName}
      </h2>
      <p>
        System Status: {systemStatus}
      </p>
      

    </article>
  )
}
